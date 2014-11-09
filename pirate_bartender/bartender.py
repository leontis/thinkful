
import random

def get_customer_prefs(customer):
    questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
    }
    preferences = {}
    inv_questions = dict((v,k) for k,v in questions.iteritems())
    for question in inv_questions.keys():
        response = raw_input(customer+", "+question+" :")
        taste = inv_questions[question]
        preferences.update({taste: response})
        #print taste, preferences[taste]

    return preferences

def construct_drink(customer,preferences): 
    drink = []
    ingredients = {
        "strong": ["glug of rum", "slug of whisky", "splash of gin"],
        "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
        "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
        "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
        "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
    }
    for preference in preferences.keys():
        if preferences[preference]== 'y':
            ingredient_list = ingredients[preference]
            #print ingredient_list
            ingredient = random.choice(ingredient_list)
            drink.append(ingredient)
    
    return drink

if __name__ == '__main__':
    customer = raw_input('What\'s yer name, Matey? :')
    print "Welcome to the Dead Man's Bar, ",customer, "!"
    print "Now I will ask ye some questions to mix ye a special poison. Jest answer \"y\" or \"n\": "
    preferences = get_customer_prefs(customer)
    drink = construct_drink(customer,preferences)
    print "drink contains: ", drink



