import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_products(self):
        sql = """
        CREATE TABLE Products (
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            Photo_Id varchar(255),
            Price varchar(255),
            Description varchar(255),
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_product(self, id: int, name: str, photo_id: str = None, price: str = None, description: str = None):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, Photo_Id, Price, Description) VALUES(1, 'John', 'shvuhbiuhidnUHIBuybIUdiuhefjnci', '122', 'bzoncksjbisjcnkj) "

        sql = """
        INSERT INTO Products(id, Name, Photo_Id, Price, Description) VALUES(?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, photo_id, price, description), commit=True)

    def select_all_products(self):
        sql = """
        SELECT * FROM Products
        """
        return self.execute(sql, fetchall=True)

    def select_product(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Products WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_products(self):
        return self.execute("SELECT COUNT(*) FROM Products;", fetchone=True)

    def update_user_price(self, price, id):

        sql = f"""
        UPDATE Products SET Price=? WHERE id=?
        """
        return self.execute(sql, parameters=(price, id), commit=True)

    def update_user_photo_id(self, photo_id, id):

        sql = f"""
        UPDATE Products SET Photo_Id=? WHERE id=?
        """
        return self.execute(sql, parameters=(photo_id, id), commit=True)

    def update_user_desc(self, desc, id):

        sql = f"""
        UPDATE Products SET Description=? WHERE id=?
        """
        return self.execute(sql, parameters=(desc, id), commit=True)

    def delete_products(self):
        self.execute("DELETE FROM Products WHERE TRUE", commit=True)

    def delete_product(self, id):
        sql = f"""
        DELETE FROM Products WHERE {id}
        """
        return self.execute(sql, commit=True)


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
