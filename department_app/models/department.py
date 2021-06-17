from department_app import db
from .employee import Employee


class Department(db.Model):
    __tablename__ = "Department"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    employees = db.relationship('Employee', backref='department', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "department name": self.name,
            "employees": [employee.name for employee in self.employees]
        }

    def __repr__(self):
        return "department : {}".format(self.name)
