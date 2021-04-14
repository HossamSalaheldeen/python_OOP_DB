import mysql.connector

class DbConnection:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", password="", autocommit=True)
        self.curr = self.conn.cursor()

    def checkConnection(self):
        if self.conn.is_connected:
            return True
        else:
            return False

    def createDatabase(self,db_name):    
        sql = f'create database if not exists {db_name}'
        self.curr.execute(sql)
        self.curr.execute("SHOW DATABASES")
        print("--------------------------Databases--------------------------")
        for x in self.curr:
            print(x)
    
    def useDatabase(self,db_name):
        use_stmt = f'USE {db_name}'
        self.curr.execute(use_stmt)

    def createTable(self,db_name,table_name):
        create_stmt = f'''create table if not exists {table_name}(
                        id int primary key not null auto_increment,
                        email varchar(50),
                        workmood varchar(50),
                        salary float,
                        is_manager boolean,
                        office_name varchar(50)
                        )'''
        self.curr.execute(create_stmt)
    
        self.curr.execute("SHOW TABLES")
        print("--------------------------Tables--------------------------")
        for x in self.curr:
            print(x)
    
    def getFieldsNames(self):
        
        select_stmt = 'select * from employee'
        self.curr.execute(select_stmt)
        columns_desc = self.curr.description
        column_names = []
        for column_desc in columns_desc:
            column_names.append(column_desc[0])
        return column_names
        # result = []
        # res = self.curr.fetchall()
        # for value in res:
        #     tmp = {}
        #     for (index,column) in enumerate(value):
        #         tmp[columns_desc[index][0]] = column
        #     result.append(tmp)
        # print(result)


    def closeConnection(self):
        self.curr.close()

    def addEmployee(self,email,workmood,salary,is_manager,office_name):
        insert_stmt = f'''Insert into employee(email, workmood, salary, is_manager, office_name)
                        values('{email}', '{workmood}', {salary}, {is_manager}, '{office_name}')'''
        self.curr.execute(insert_stmt)

    def getAllEmployees(self):
        select_stmt = 'select * from employee'
        self.curr.execute(select_stmt)
        res = self.curr.fetchall()
        columns_desc = self.curr.description
        column_names = []
        for column_desc in columns_desc:
            column_names.append(column_desc[0])
        return column_names , res
        

    def getEmployee(self,empid):
        search_stmt = f'select * from employee where id = {empid}'
        self.curr.execute(search_stmt)
        res = self.curr.fetchall()
        columns_desc = self.curr.description
        column_names = []
        for column_desc in columns_desc:
            column_names.append(column_desc[0])
        return column_names , res

    def deleteEmployee(self,empid):
        delete_stmt = f'delete from employee where id = {empid}'
        self.curr.execute(delete_stmt)
    