class Employee:
    def employeeDetails(self):
        self.name = "Matthew"
        print("Name = ", self.name)
        age = 30   #not using the self parameter means age can't be used
        print("age = ", age)                        #outside of this class.

    def printEmployeeDetails(self):
        print("Printing in another method")
        print("Name= ", self.name)
        print("Age =", age)

employee = Employee()
employee.employeeDetails()
employee.printEmployeeDetails()  #will not recognise age as haven't used self
                                 #parameter.
