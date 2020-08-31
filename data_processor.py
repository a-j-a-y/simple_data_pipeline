import psycopg2
import requests

connection = psycopg2.connect("dbname='simple_data_pipeline' user='ajay' host='localhost' password='newpass'")
cursor = connection.cursor()
insert_query_template = "INSERT INTO employee_details (name, ssn) VALUES ('{name_value}', '{ssn_value}')"
while True:
    response = requests.get("http://127.0.0.1:5000/4")
    for data_values in response.json()['data']:
        insert_query = insert_query_template.format(name_value=data_values[0], ssn_value=data_values[1])
        cursor.execute(insert_query)
        connection.commit()
        print(insert_query)

cursor.close()
connection.close()
