from department_app import db

from department_app.models.department import Department
from department_app.models.employee import Employee

from datetime import date


def populate_db():
    department1 = Department(name="Research and development")
    department2 = Department(name="Marketing")

    employee1 = Employee(
        name="Aida",
        date_of_birth=date(1985, 10, 15),
        salary=1500
    )

    employee2 = Employee(
        name="Arthur",
        date_of_birth=date(1989, 4, 5),
        salary=1100
    )

    department1.employees.append(employee1)
    department2.employees.append(employee2)
    db.session.add_all([department1, department2])
    db.session.add_all([employee1, employee2])
    db.session.commit()


if __name__ == '__main__':
    populate_db()
