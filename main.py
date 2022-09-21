import sqlite3


def sqlite_f():
    try:
        sqlite_connection = sqlite3.connect('chinook.db')
        cursor = sqlite_connection.cursor()
        print("База данных создана и успешно подключена к SQLite")

        sqlite_select_query = "SELECT FirstName, COUNT(FirstName) FROM Customers GROUP BY FirstName;"
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        print(record)
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

sqlite_f()