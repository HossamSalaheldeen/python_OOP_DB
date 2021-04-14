import employee
import office
def menu(options,*args):
    for option in range(0,options):
        print("[" + str(option + 1) + "] " + args[option])

emp = employee.Employee()
office = office.Office()
 
menu1_option_num = 3
menu(menu1_option_num,"Enter as manager: ","Enter as normal employee:","Exit")
menu1_option = int(input("Enter your option: "))

while menu1_option != menu1_option_num:
    if menu1_option == 1:
        menu2_option_num = 5
        menu(menu2_option_num,"Show all employees","Show employee","Hire employee","Fire employee","Back")
        menu2_option = int(input("Enter your option: "))
        while menu2_option != menu2_option_num:
            if menu2_option == 1:
                office.get_all_employees()
            elif menu2_option == 2:
                empId = int(input("Enter employee Id: "))
                office.get_employee(empId)
            elif menu2_option == 3:
                emp = employee.Employee()
                emp.email = input("Enter employee email: ")
                emp.workmood = input("Enter employee workmood: ")
                emp.salary = int(input("Enter employee salary: "))
                check = input("Enter is_manager? mngr or nrml?")
                if check == "mngr":
                    emp.is_manager =  True
                if check == "nrml":
                    emp.is_manager =  False
                emp.office_name = input("Enter employee office name: ")
                office.hire(emp)
                print("Added employee successfully.")
            elif menu2_option == 4:
                empid = int(input("Enter employee Id: "))
                office.fire(empid)
                print("removed employee successfully.")
            else:
                print("Invalid option")

            print("\n")
            menu(menu2_option_num,"Show all employees","Show employee","Hire employee","Fire employee","Back")
            menu2_option = int(input("Enter your option: "))

    elif menu1_option == 2:
        menu3_option_num = 3
        menu(menu3_option_num,"Show all employees","Show employee","Back")
        menu3_option = int(input("Enter your option: "))
        while menu3_option != menu3_option_num:
            if menu3_option == 1:
                office.get_all_employees()
            elif menu3_option == 2:
                empId = int(input("Enter employee Id: "))
                office.get_employee(empId)
            else:
                print("Invalid option")

            print("\n")
            menu(menu3_option_num,"Show all employees","Show employee","Back")
            menu3_option = int(input("Enter your option: "))
    else:
        print("Invalid option")

    print("\n")
    menu(menu1_option_num,"Enter as manager: ","Enter as normal employee:","Exit")
    menu1_option = int(input("Enter your option: "))

print("Exiting.........")