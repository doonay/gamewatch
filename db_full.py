# На вход передаем список массивов
# Каждый массив - набор данных одной игры (карточка)
import sqlite3

""" Создание, либо открытие существующей базы (в файле) """
def db_create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn

""" Создание, либо открытие существующей таблицы """
def db_create_table(conn, table_name):
  cur = conn.cursor()
  cur.execute("""CREATE TABLE IF NOT EXISTS """ + table_name + """(
    name TEXT,
    data TEXT,
    img_link TEXT);
  """)
  conn.commit()

""" Добавление данных в таблицу """
def db_data_add(conn, list_of_games): #list of cortages
  cur = conn.cursor()
  cur.executemany("INSERT INTO games VALUES(?, ?, ?);", list_of_games)
  conn.commit()

""" Получение всех данных из таблицы """
def db_select_all_data(table_name):
  #Функцию fetchall() можно использовать для получения всех результатов.
  conn = db_create_connection('database.db')
  with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM " + table_name)
    all_results = cur.fetchall()

  return all_results

""" Удаление данных в SQLite в Python """
def db_delete_data(conn, name):
  # Предположим, нужно удалить любого пользователя с фамилией «Parker».
  cur = conn.cursor()
  cur.execute("DELETE FROM games WHERE name='" + name + "';")
  conn.commit()

#-------------------------------------------------- TESTS ------------------------------------------

def main():

  """ Создание, либо открытие существующей базы (в файле) """
  database = "database.db"
  conn = db_create_connection(database)

  """ Создание, либо открытие существующей таблицы """
  with conn:
    # create a new table
    table_name = 'games'
    project_id = db_create_table(conn, table_name)

  """ Добавление данных в таблицу """
  list_of_games = [
    ('Stephanie', 'Stewart', 'female'), ('Sincere', 'Sherman', 'female'), ('Sidney', 'Horn', 'male'), 
    ('Litzy', 'Yates', 'female'), ('Jaxon', 'Mills', 'male'), ('Paul', 'Richard', 'male'), 
    ('Kamari', 'Holden', 'female'), ('Gaige', 'Summers', 'female'), ('Andrea', 'Snow', 'female'), 
    ('Angelica', 'Barnes', 'female'), ('Leah', 'Pitts', 'female'), ('Dillan', 'Olsen', 'male'), 
    ('Joe', 'Walsh', 'male'), ('Reagan', 'Cooper', 'male'), ('Aubree', 'Hogan', 'female'), 
    ('Avery', 'Floyd', 'male'), ('Elianna', 'Simmons', 'female'), ('Rodney', 'Stout', 'male'), 
    ('Elaine', 'Mcintosh', 'female'), ('Myla', 'Mckenzie', 'female'), ('Alijah', 'Horn', 'female'),
    ('Rohan', 'Peterson', 'male'), ('Irene', 'Walters', 'female'), ('Lilia', 'Sellers', 'female'), 
    ('Perla', 'Jefferson', 'female'), ('Ashley', 'Klein', 'female')
  ]

  with conn:
    db_data_add(conn, list_of_games)

  """ Получение всех данных из таблицы """
  with conn:
    db_select_all_data(conn, 'games')

  print('-------------- Удаляем Stephanie. Проверяем: --------------')
  """ Удаление данных в SQLite в Python """
  with conn:
    db_delete_data(conn, 'Stephanie')
  """ Получение всех данных из таблицы """
  with conn:
    db_select_all_data(conn, 'games')


if __name__ == '__main__':
  main()