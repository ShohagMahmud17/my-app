def init_db(mysql):
    cursor = mysql.connection.cursor()
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS tasks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            task VARCHAR(255) NOT NULL
        )
    ''')
    mysql.connection.commit()

