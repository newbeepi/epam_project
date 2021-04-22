from department_app import db
from department_app.models.department import Department
from department_app.models.employee import Employee


def insert_department(name):
    department = Department(name)
    db.session.add(department)
    db.session.commit()


def delete_department_by_name(name):
    department = db.session.query(Department).filter_by(name=name).first()
    db.session.delete(department)
    db.session.commit()


def delete_department_by_id(id):
    department = db.session.query(Department).filter_by(id=id).first()
    db.session.delete(department)
    db.session.commit()


def add_employee(name, **kwargs):
    department = Department(name)
    employee = Employee(**kwargs)
    department.employees.append(employee)
    db.session.add(department)
    db.session.add(employee)
    db.session.commit()