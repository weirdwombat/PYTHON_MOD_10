"""
Program : customer.py
Author : Olivia Kennedy
Date Last Modified : 07/08/2020
This program has the class customer that requires the input of a last name, a first_name, cid
phone number and address. This info is then printed line by line. The Cid must be numeric input.
"""
class Customer:
    def __init__(self, lname, fname, cid, phone, a_1, a_2):
        self.last_name = lname
        self.first_name = fname
        self.customer_id = cid
        self.phone_number = phone
        self.address_1 = a_1
        self.address_2 = a_2

    def set_last_name(self, lname):
        self.last_name = lname

    def set_first_name(self, fname):
        self.first_name = fname

    def set_customer_id(self, cid):
        self.customer_id = cid

    def set_phone_number(self, phone):
        self.phone_number = phone

    def display(self):
        """
        :return: Multiple lines telling the customers last name, first name,
        their cid, phone number, and address.
        """
        return str(self.last_name) + ", " + str(self.first_name) + "\n" + ("CID: ") + str(self.customer_id) + "\n" + ("Phone Number: ") + str(self.phone_number) + "\n" + str(self.address_1) + "\n" + str(self.address_2)



if __name__ == '__main__':
    customer_1 = Customer('Doe', 'John', 1234, '515-8675-309', "789 Fake St", "Des Moines, Iowa 50309")
    print(customer_1.display())
    try:
        customer_2 = Customer('Smith', 'Bob', 'OOl', '1-800-FlO-WERS', '1600 Pennsylvania Ave NW', 'Washington, DC 20500')
        if not isinstance(customer_2.customer_id, int):
            raise AttributeError
    except AttributeError as error:
        #attribute error was raised for non-numeric input for the CID
        print("Please enter numeric input for the CID", error)




