from flask import request
from flask_restful import Resource

from department_app.exceptions import EmployeeNotFound
from department_app.schemas.employee_schema import EmployeeSchema
from department_app.service.employee_service import read_one_employee, delete_employee, update_employee, read_employees, \
    create_employee

from datetime import date


class EmployeeApi(Resource):
    def get(self, id):
        try:
            employee = read_one_employee(id)
            return {"message": "Success", "employee": employee.to_dict()}, 200
        except EmployeeNotFound:
            return {"message": "Employee not found"}, 204

    def put(self, id):
        data_json = request.get_json(force=True)
        if data_json.get('date_of_birth', None):
            date_of_birth = date.fromisoformat(data_json['date_of_birth'])
            data_json['date_of_birth'] = date_of_birth
        try:
            employee = update_employee(id, **data_json)
            return {"message": "Success", "employee": employee.to_dict()}, 200
        except EmployeeNotFound:
            return {"message": "Employee not found"}, 204

    def delete(self, id):
        try:
            employee = delete_employee(id)
            return {"message": "Success", "employee": employee.to_dict()}, 200
        except EmployeeNotFound:
            return {"message": "Employee not found"}, 204


class EmployeeListApi(Resource):
    def post(self):
        data_json = request.get_json(force=True)
        date_of_birth = date.fromisoformat(data_json['date_of_birth'])
        data_json['date_of_birth'] = date_of_birth
        department_id = data_json.get('department_id', None)
        if department_id:
            data_json.pop('department_id')
        try:
            employee = create_employee(department_id, **data_json)
            return {"message": "Success", "employee": employee.to_dict()}, 201
        except EmployeeNotFound:
            return {"message": "Employee not found"}, 204

    def get(self):
        try:
            employees = read_employees()
            return {"message": "Success", "employees": [employee.to_dict() for employee in employees]}, 200
        except EmployeeNotFound:
            return {"message": "Employee Not Found"}, 204
