from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

import sqlalchemy as sa 

from sqlalchemy.orm import sessionmaker

import pdb   
import logging
log = logging.getLogger(__name__)

################################################################################
# set up logging - see: https://docs.python.org/2/howto/logging.html

# when we get to using Flask, this will all be done for us
import logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
log.addHandler(console_handler)

################################################################################
# Domain Model

Base = declarative_base()
log.info("base class generated: {}".format(Base) )

# define our domain model
class Species(Base):
    """
    domain model class for a Species
    """
    __tablename__ = 'species'

    # database fields
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    breeds = relationship('Breed', backref="species")

    # methods
    def __repr__(self):
        return self.name                   

class Breed(Base):
    """
    domain model class for a Breed
    has a many-to-one relationship Species
    """
    __tablename__ = 'breed'

    # database fields
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    species_id = Column(Integer, ForeignKey('species.id'), nullable=False ) 
    pets = relationship('Pet', backref="breed")
          
    # methods
    def __repr__(self):
        return "{}: {}".format(self.name, self.species) 
 
class Pet(Base):
    """ Domain model class for a Pet
    Has a many-to-one relationship with breed
    has a name, age, adopted attribute (Boolean), breed_id, and shelter_id
    pets must have a breed but may or may not have a shelter
    """
    __tablename__ = 'pet'
    # database fields
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    breed_id = Column(Integer, ForeignKey('breed.id'),nullable = False)
    age = Column(Integer,nullable = True)
    adopted = Column(Boolean)
    shelter_id = Column(Integer, ForeignKey('shelter.id'), nullable = True)

    #methods
    def __repr__(self):
        return "{} {} {} {}".format(self.name, self.breed, self.age, self.shelter)

class Shelter(Base):
    __tablename__ = 'shelter'
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    web_site = Column(Text,nullable = False)
    #methods
    def __repr__(self):
        return "{}: {}".format(self.name, self.website)


################################################################################
def init_db(engine):
    "initialize our database, drops and creates our tables"
    log.info("init_db() engine: {}".format(engine) )
    
    # drop all tables and recreate
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    log.info("  - tables dropped and created")



if __name__ == "__main__":
    log.info("main executing:")              

    # create an engine
    # TODO: allow passing in a db connection string from a command line arg
    engine = create_engine('sqlite:///./pet_db1')
    #engine = create_engine('sqlite:///:memory:')
    log.info("created engine: {}".format(engine) )

    # if we asked to init the db from the command line, do so
    if True:
        init_db(engine)

    # call the sessionmaker factory to make a Session class 
    Session = sessionmaker(bind=engine)
    
    # get a local session for the this script
    db_session = Session()
    log.info("Session created: {}".format(db_session) )
   
    # count our starting species & breeds
    num_species = db_session.query(Species).count()
    num_breeds = db_session.query(Breed).count()
    log.info("starting with {} species and {} breeds".format(num_species, num_breeds) )

    log.info("Creating Species: Cat and Dog (Transient)")
    cat = Species(name="Cat")
    dog = Species(name="Dog")
    
    # we can verify that cat and dog do not have ids yet.
    assert cat.id == None
    assert dog.id == None
    log.info("Type of cat.id is {}. Type of dog.id is {}".format(type(cat.id), type(dog.id) ))


    # add them to the session and commit to save to db
    log.info("Adding dog and cat to session and committing.")    
    db_session.add_all( [cat, dog] )
    db_session.commit()

    # now they have ids
    assert cat.id != None
    assert dog.id != None
    log.info("Now the type of cat.id is {} and type of dog.id is {}".format(type(cat.id), type(dog.id) ))
 
    # let's use that id to make a breed
    log.info("Creating three new dog breeds: Poodle, Labrador Retriever, and Golden Retriever")
    poodle = Breed(name='Poodle', species_id=dog.id)
    lab = Breed(name='Labrador Retriever', species_id=dog.id)
    golden = Breed(name='Golden Retriever', species_id=dog.id)
    pomeranian = Breed(name= 'Pomeranian', species_id=dog.id)
    tabby = Breed(name = 'Tabby', species_id=cat.id)

    # dog.breeds is still empty, as we have saved the above
    log.info("New breeds created, but still transient. There are {} dog breeds in the database".format(
        len(dog.breeds)))
    log.info("New breeds created, but still transient. There are {} cat breeds in the database".format(
        len(cat.breeds)))
    
    assert dog.breeds == []
    assert cat.breeds == []
    db_session.add_all( [poodle, lab, golden, pomeranian, tabby] )
    db_session.commit()

    # now dog.breeds contains lab, poodle, & golden
    # we can use set to assert on membership disregarding order in list
    assert set( [poodle,lab,golden, pomeranian] ) == set( dog.breeds )
    log.info("New breeds saved. There are now {} dog breeds in the database".format(
        len(dog.breeds)))
   
    # Now let's see how SQLAlchemy let's us assign objects as foreign keys even if those
    # objects have not yet been saved.   l

    # Let's make a new species, parrot and a new breed, Norwegian Blue.
    # But instead of building our relationship with the 'species_id' field,
    # we will use the 'species' relationship. We can use the species parrot, 
    # even though it has no ID and has not yet been persisted. 
    # SQLAlchemy's Identity Map can manage all of this

    log.info("Demonstrating the smarts of the Identity Map")
    log.info("There are currently {} parrot species in the db".format(
        db_session.query(Species).filter(Species.name=='Parrot').count() ) )
    log.info("Creating new breed, Norwegian Blue, which is of the Parrot Species")
    norwegian_blue = Breed(name="Norwegian Blue",
        species=Species(name="Parrot")  )
    parrot = norwegian_blue.species
    
    log.info("Type of parrot.id is {} and norwegian_blue.id is {}".format(
        type(parrot.id), type(norwegian_blue.id) ) )
    log.info("But norwegian_blue.species is: {}".format(norwegian_blue.species))
    log.info("And parrot.breeds is {}".format(parrot.breeds))
    assert norwegian_blue.species == parrot
    assert norwegian_blue in parrot.breeds 

    log.info('Now lets add parrot to the session and commit, and we\'ll get' +\
        ' our new breeds for free.')
    log.info('adding and committing parrot to session') 
    db_session.add(parrot)
    db_session.commit()
    
    log.info("Now parrot.id is {} and norwegian_blue.id is {}".format(
        parrot.id, norwegian_blue.id))    
    log.info("Now cat.id is {} and tabby.id is {}".format(
        cat.id, tabby.id))    
    log.info("Now dog.id is {} and pomeranian.id is {}".format(
        dog.id, pomeranian.id))    
    
    # Next, add two shelters to the database. The first shelter's name is "NYC Pet Orphanage",
    # and its website is "http://www.nyc-pet-orphanage.com. The second shelter's name is "New Orleans Pet Hotel" and 
    # its website is "http://www.neworleanspethotel.com". 
    # Add the shelters to the db and commit.
 
    nyc_pet_orphanage = Shelter(name="NYC Pet Orphanage", web_site = "http://www.nyc-pet-orphanage.com")
    neworleanspethotel = Shelter(name="New Orleans Pet Hotel", web_site = "http://www.neworleanspethotel.com")
    db_session.add_all( [nyc_pet_orphanage, neworleanspethotel] )
    db_session.commit()
    log.info("Now nyc_pet_orphanage.id is {} and neworleanspethotel.id is {}".format(
        nyc_pet_orphanage.id, neworleanspethotel.id))

    # Next make two pets. First make a Golden Retriever named "Thomas" who is 5, not adopted,
    # and at the NYC pet orphanage. Then, make a poodle named "Sue" who is 8, adopted, and
    # has no shelter.

    thomas = Pet(name = "Thomas", breed = golden, age = 5, adopted = False)
    sue = Pet(name = "Sue", breed = poodle, age = 8, adopted = True)

    db_session.add_all( [thomas, sue] )
    db_session.commit()

    log.info("Now thomas.breed is {} and sue.breed is {}".format(
        thomas.breed, sue.breed))
    log.info("Now thomas.adopted is {} and sue.adopted is {}".format(
        thomas.adopted, sue.adopted))

    
    # Finally, print a log message that indicates how many pets, breeds, and species 
    # we have in the database   
    #################################################
    #  Now it's up to you to complete this script ! #
    #################################################
    
    # For each of the following steps, be sure to use log to print out feedback
    # about what's happening.


    # Define a Pet class up above in this script with the other class definitions.
    # Pet should have a name, age, adopted attribute (which is boolean), breed_id, and shelter_id. 

    # Also define a Shelter class. Shelters should have a name and website address.
    # Keep in mind that a pet *must* have a breed, but it may or may not have a shelter.

    # Next, add two shelters to the database. The first shelter's name is "NYC Pet Orphanage",
    # and its website is "http://www.nyc-pet-orphanage.com. The second shelter's name is "New Orleans Pet Hotel" and 
    # its website is "http://www.neworleanspethotel.com". 
    # Add the shelters to the db and commit.


    # Next make two pets. First make a Golden Retriever named "Thomas" who is 5, not adopted,
    # and at the NYC pet orphanage. Then, make a poodle named "Sue" who is 8, adopted, and
    # has no shelter.
    
    # Finally, print a log message that indicates how many pets, breeds, and species 
    # we have in the database   
  
    db_session.close()
    log.info("all done!")
