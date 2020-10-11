import create_widgets
import mysql.connector


def create_project(name_of_the_project, project_description):

    name_of_the_project_init = name_of_the_project.get()
    project_description_init = project_description.get("1.0", "end")

    conn = mysql.connector.connect(host="localhost", user="root", password="suchith")
    cursor = conn.cursor()
    cursor.execute("use programmer_diary")
    print("db initiated successfully")
    print("table created")
    query = """INSERT INTO projects(project_name, project_desc)
                        VALUES(%s,%s);"""
    list_to_be_passed = (name_of_the_project_init, project_description_init)
    cursor.execute(query, list_to_be_passed)
    conn.commit()
    cursor.close()
    conn.close()
    print("Done")


def create_new_issue(project_name, issue_state, issue_name, issue_text):
    conn = mysql.connector.connect(host="localhost", user="root", password="suchith")
    cursor = conn.cursor()
    cursor.execute("use programmer_diary")

    tuple_to_be_inserted = []
    tuple_to_be_inserted.append(project_name)
    tuple_to_be_inserted = tuple(tuple_to_be_inserted)
    q = """select project_id from projects where project_name = %s"""
    print(tuple_to_be_inserted)
    cursor.execute(q, tuple_to_be_inserted)
    id = cursor.fetchall()
    id = id[0]
    project_id = id[0]
    list_to_be_inserted = (project_id, issue_name, issue_text)
    print(list_to_be_inserted)
    insert_query = """INSERT INTO issues(project_id, issue_name, issue_desc)
                        VALUES(%s, %s, %s);"""

    cursor.execute(insert_query, list_to_be_inserted)
    conn.commit()
    cursor.close()
    conn.close()


def get_projects_from_database():
    conn = mysql.connector.connect(host="localhost", user="root", password="suchith")
    cursor = conn.cursor()
    cursor.execute("use programmer_diary")
    query = """SELECT project_name FROM projects;"""
    cursor.execute(query)
    records = cursor.fetchall()
    print(records)
    cursor.close()
    conn.close()
    return records


def get_issues_from_database(project_name):
    conn = mysql.connector.connect(host="localhost", user="root", password="suchith")
    cursor = conn.cursor()
    cursor.execute("use programmer_diary")
    tuple_to_be_inserted = []
    tuple_to_be_inserted.append(project_name)
    tuple_to_be_inserted = tuple(tuple_to_be_inserted)
    print(project_name)
    q = """select project_id from projects where project_name = %s"""
    cursor.execute(q, tuple_to_be_inserted)
    id = cursor.fetchall()
    id = id[0]
    query = """SELECT issue_name FROM issues WHERE project_id = %s """
    cursor.execute(query, id)
    record = cursor.fetchall()
    print(record)
    cursor.close()
    conn.close()
    return record


def post_solution_to_database(project_name, issue_name, project_description):
    conn = mysql.connector.connect(host="localhost", user="root", password="suchith")
    cursor = conn.cursor()
    cursor.execute("use programmer_diary")

    tuple_to_be_inserted = []
    tuple_to_be_inserted.append(issue_name)
    tuple_to_be_inserted = tuple(tuple_to_be_inserted)
    q = """select issue_id from issues where issue_name = %s"""
    cursor.execute(q, tuple_to_be_inserted)
    id = cursor.fetchall()
    id = id[0]
    issue_id = id[0]
    print("issue_id is in the next line")
    print(issue_id)
    list_to_be_inserted = [issue_id, project_description]
    tuple_to_be_inserted = tuple(list_to_be_inserted)
    insert_query = """INSERT INTO steps(issue_id, steps_name)
                    VALUES(%s, %s);"""
    cursor.execute(insert_query, tuple_to_be_inserted)
    print("DONE !!!")
    conn.commit()
    cursor.close()
    conn.close()


def view_solution(issue_name, frame):
    conn = mysql.connector.connect(host="localhost", user="root", password="suchith")
    cursor = conn.cursor()
    cursor.execute("use programmer_diary")

    tuple_to_be_inserted = []
    tuple_to_be_inserted.append(issue_name)
    tuple_to_be_inserted = tuple(tuple_to_be_inserted)
    q = """select issue_id from issues where issue_name = %s"""
    cursor.execute(q, tuple_to_be_inserted)
    id = cursor.fetchall()
    id = id[0]

    query = """SELECT steps_name, time_of_creation FROM steps WHERE issue_id = %s"""
    cursor.execute(query, id)
    records = cursor.fetchall()
    create_widgets.create_new_window(records)
    cursor.close()
    conn.close()