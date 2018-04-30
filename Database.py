import pymysql


def read_from_db():
    """
    Reading task list from a DB
    :return: a list of tasks
    """
    lista = list()
    # prepare the query for reading from DB
    query = "SELECT * FROM task"

    # connectione to database
    connection = pymysql.connect(user="root", password="Matrix9697", host="localhost", database="first")

    # get a cursor
    cursor = connection.cursor()

    # execute query
    cursor.execute(query)

    # fetch result from query
    results = cursor.fetchall()
    print(results)
    x = dict()
    print(x)

    # close cursor and connection
    cursor.close()
    connection.close()
    return results


def insert_new_task(newTask):
    """
    Function for insert a new task to the list and rewrite the list to a new file
    :param bot:
    :param received:
    :param args:
    :return:
    """

    query = "INSERT INTO task (todo) VALUES (%s)"

    # connectione to database
    connection = pymysql.connect(user="root", password="Matrix9697", host="localhost", database="first")

    cursor = connection.cursor()

    cursor.execute(query, (newTask,))

    connection.commit()

    cursor.close()
    connection.close()

def delete_task(id_task):

    query= "DELETE FROM task WHERE id_task=(%s)"

    # connectione to database
    connection = pymysql.connect(user="root", password="Matrix9697", host="localhost", database="first")

    cursor = connection.cursor()

    cursor.execute(query, (id_task,))

    connection.commit()

    cursor.close()
    connection.close()