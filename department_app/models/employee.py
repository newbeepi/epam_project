from department_app import db


class Employee(db.Model):
    __tablename__ = 'Employee'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    salary = db.Column(db.Float, default=1200)
    department_id = db.Column(db.Integer, db.ForeignKey('Department.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth date": self.date_of_birth,
            "salary": self.salary,
        }

    def __repr__(self):
        return "Name: {}, date of birth: {}, salary: {}".format(self.name, self.date_of_birth, self.salary)

