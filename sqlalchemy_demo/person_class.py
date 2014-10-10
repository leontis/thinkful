class Person(base):
    # boilerplate ommitted here -- we'll cover that later

    # phone number accessing property, reading Person.phone will call this.
    # the property just deals with the presentation of the underlying, private
    # data variable, _phone
    @property
    def phone(self):
        """return phone number formatted with hyphens"""
        # get the phone number from the database, mapped to private self._phone
        num = self._phone
        # return a formatted version using hyphens
        return "%s-%s-%s" % (num[0:3], num[3:6], num[6:10])

    # phone number writing property, writing to public Person.phone calls this
    @phone.setter
    def phone(self, value):
        """store only numeric digits, raise exception on wrong number length"""
        # get rid of any hyphens
        number = value.replace('-', '')
        # get rid of any spaces
        number = number.replace(' ', '')
        # check length, raise exception if bad
        if len(number) != 10:
            raise BadPhoneNumberException("Phone number not 10 digits long")
        else:
            # write the value to the property that automatically goes to DB
            self._phone = number
            