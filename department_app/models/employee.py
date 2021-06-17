from department_app import db


class Employee(db.Model):
    __tablename__ = 'Employee'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), nullable=False)
    surname = db.Column(db.String(32), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    salary = db.Column(db.Float, default=0)
    department_id = db.Column(db.Integer, db.ForeignKey('Department.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "birth date": self.date_of_birth.isoformat(),
            "salary": self.salary,
            "department": self.department.name if self.department is not None else "unemployed"
        }

    def __repr__(self):
        return "Name: {}, date of birth: {}, salary: {}".format(self.name, self.date_of_birth, self.salary)

