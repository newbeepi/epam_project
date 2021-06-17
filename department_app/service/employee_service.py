from department_app import db
from department_app.exceptions import EmployeeNotFound

from department_app.models.employee import Employee
from department_app.models.department import Department

from typing import List


def create_employee(department_id=None, **fields) -> Employee:
    employee = Employee(**fields)
    if department_id:
        department = db.session.query(Department).get(department_id)
        department.employees.append(employee)
    db.session.add(employee)
    db.session.commit()
    return employee


def read_one_employee(id) -> Employee:
    employee = db.session.query(Employee).get(id)
    if not employee:
        raise EmployeeNotFound
    return employee


def read_employees() -> List[Employee]:
    employees = db.session.query(Employee).all()
    if not employees:
        raise EmployeeNotFound
    return employees


def update_employee(id, **fields) -> Employee:
    employee = read_one_employee(id)
    if 'department_id' in fields:
        department = db.session.query(Department).get(fields['department_id'])
        employee.department = department
    elif fields['name']:
        employee.name = fields['name']
    elif fields['surname']:
        employee.surname = fields['surname']
    elif fields['date_of_birth']:
        employee.date_of_birth = fields['date_of_birth']
    elif fields['salary']:
        employee.salary = fields['salary']
    db.session.commit()
    return employee


def delete_employee(id) -> Employee:
    employee = read_one_employee(id)
    db.session.delete(employee)
    db.session.commit()
    return employee