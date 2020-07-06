from datetime import datetime

class Employee:
    '''Employee Class '''
    # Constructor
    def __init__(self, lname, fname, address_1, address_2, phone_number, salaried, start_date, salary):
         self.last_name = lname
         self.first_name = fname
         self.address_1 = address_1
         self.address_2 = address_2
         self.phone_number = phone_number
         self.salaried = salaried
         self.start_date = start_date
         self.salary = salary

    def set_last_name(self, lname):
        self.last_name = lname

    def set_first_name(self, fname):
        self.first_name = fname

    def set_salaried(self, salaried, salary):
        if salaried == "Salaried Employee":
            return 'Salaried Employee: ' +  str(salary) +" "+ 'per year'
        else:
            return 'Hourly Employee: ' + str(salary) + 'per hour'

    def set_starting_date(self, start_date):
        dt = start_date
        return dt.strftime("%m-%d-%y")

    def display(self):
        return str(self.last_name) + ", " + str(self.first_name) + "\n" + str(self.address_1) + "\n" + str(self.address_2) + "\n" + (self.set_salaried(self.salaried, self.salary)) + "\n" +"Start Date:" +" "+ (self.set_starting_date(self.start_date))
         # spacing has not been implemented yet for purposes of simplicity - I do know how to do that.

# Driver
emp = Employee('Patel', 'Sasha', '123 Main St', 'Urban, Iowa', '515-867-5309', 'Salaried Employee', datetime(2020, 4, 27), '$40,000')   # call the construtor, needs to have a first and last name in parameter
print(emp.display())             # display returns a str, so print the information
