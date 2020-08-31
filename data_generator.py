from flask import Flask
from faker import Faker

app = Flask(__name__)
fake = Faker()


@app.route('/<int:x>')
def data_generator(x):
    data = []
    for i in range(0, x):
        data.append([fake.name(), fake.profile()['ssn']])
    return {"data": data}



