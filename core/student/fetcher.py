

# Setting up connection with the database with connector
db = pymysql.connector.connect(
        host="localhost",
        port="3308",
        user="root",
        password="",
        database="orm_series"
    )

    # Adding the columns in the connector
columns = [
    "firstName VARCHAR(100)",
    "surname VARCHAR(100)",
    "age INT(11)",
    "classroom INT(11)",
    "teacher VARCHAR(100)",
]