import dbconnection 
import employee
class Office:
    def __init__(self):
        self._name = None
        self._employees = None

#name attribute setter & getter
#-------------------------------
    @property
    def name(self):
        return self._name

    @name.setter   
    def name(self, name):
        self._name = name

#employees attribute setter & getter
#--------------------------------
    @property
    def employees(self):
        return self._employees

    @employees.setter   
    def email(self, employees):
        self._employees = employees

    def get_all_employees(self):
        db = dbconnection.DbConnection()
        if db.checkConnection():
            db.useDatabase('python_lab') 
            print("employees data")
            print("-" * 10)
            column_names , emps = db.getAllEmployees()
            for column_name in column_names:
                print(column_name, end=" ")
            
            print()
            
            for emp in emps:
                if emp[4] == 1:
                    print(*emp[0:3],*emp[4:], sep = ", ", end="")
                    print()
                else:
                    print(*emp, sep = ", " , end="")
                    print()
              
        else:
            print("connection failed")
        db.closeConnection()
    
    def get_employee(self,empId):
        db = dbconnection.DbConnection()
        if db.checkConnection():
            db.useDatabase('python_lab')
            print("employees data")
            print("-" * 10)
            column_names , emps = db.getEmployee(empId)
            print('(',end="")
            for column_name in column_names:
                print(column_name, end=" ")
            print(')')
            print('(',end="")
            for emp in emps:
                if emp[4] == 1:
                    print(*emp[0:3],*emp[4:], sep = ", ", end="")
                else:
                    print(*emp, sep = ", " , end="")
            print(')')
        else:
            print("connection failed")
        db.closeConnection()

    def hire(self,employee):
        db = dbconnection.DbConnection()
        if db.checkConnection():
            db.useDatabase('python_lab')
            db.addEmployee(employee.email,employee.workmood,employee.salary,employee.is_manager,employee.office_name)
        else:
            print("connection failed")
        db.closeConnection()


    def fire(self,empId):
        db = dbconnection.DbConnection()
        if db.checkConnection():
            db.useDatabase('python_lab')
            db.deleteEmployee(empId)
        else:
            print("connection failed")
        db.closeConnection()




