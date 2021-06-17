from department_app import app, api

from department_app.rest.employee import EmployeeApi, EmployeeListApi
from department_app.rest.department import DepartmentApi, DepartmentListApi

from department_app.models.employee import Employee
from department_app.models.department import Department

from department_app.routes import *


api.add_resource(EmployeeListApi, '/employee', strict_slashes=False)
api.add_resource(EmployeeApi, '/employee/<id>', strict_slashes=False)
api.add_resource(DepartmentListApi, '/department', strict_slashes=False)
api.add_resource(DepartmentApi, '/department/<id>', strict_slashes=False)


if __name__ == '__main__':
    app.run()
