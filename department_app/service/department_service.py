from department_app import db
from department_app.exceptions import DepartmentNotFound
from department_app.models.department import Department

from typing import List


def create_department(**fields) -> Department:
    department = Department(**fields)
    db.session.add(department)
    db.session.commit()
    return department


def read_one_department(id) -> Department:
    department = db.session.query(Department).get(id)
    if not department:
        raise DepartmentNotFound
    return department


def read_departments() -> List[Department]:
    departments = db.session.query(Department).all()
    if not departments:
        raise DepartmentNotFound
    return departments


def update_department(id, **kwargs) -> Department:
    department = read_one_department(id)
    department.update(**kwargs)
    db.session.commit()
    return department


def delete_department(id) -> Department:
    department = read_one_department(id)
    db.session.delete(department)
    db.session.commit()
    return department
