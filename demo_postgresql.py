from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    "postgresql://admin:postgresql33333333@127.0.0.1:5432/testdb"

db = SQLAlchemy(app)

class Students(db.Model):

    __tablename__ = "Students"
    sid  = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    tel  = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    email= db.Column(db.String(100))

    def __init__(self, name, tel, addr, email):
        self.name = name
        self.tel = tel
        self.addr = addr
        self.email= email

@app.route("/")
def index():
    db.create_all()
    return "db connect success!!!"

@app.route("/insert")
def insert():
    student = Students("Alice", "0911111111", "Taipei", "aaa@aaa")
    db.session.add(student)
    db.session.commit()
    return "add success"

@app.route("/insertAll")
def insertAll():
    student1 = Students("Betty", "0922222222", "Taijon", "bbb@bbb")
    student2 = Students("Clare", "0933333333", "Tainan", "ccc@ccc")
    student = (student1, student2)
    db.session.add_all(student)
    db.session.commit()
    return "all add success"

if __name__ == "__main__":
    app.run(debug = True, port = 5002)









    



