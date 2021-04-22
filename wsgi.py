from department_app import app, api

from department_app.rest.employee import EmployeeApi
from department_app.rest.department import DepartmentApi

from department_app.models.employee import Employee
from department_app.models.department import Department


api.add_resource(EmployeeApi, '/employee', '/employee/<id>', strict_slashes=False)
api.add_resource(DepartmentApi, '/department', '/department/<id>', strict_slashes=False)


if __name__ == '__main__':
    app.run()
