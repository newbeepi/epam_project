from flask_restful import Resource

from flask import request

from department_app.exceptions import DepartmentNotFound
from department_app.schemas.department_schema import DepartmentSchema
from department_app.service.department_service import delete_department, read_departments, read_one_department, \
    update_department, create_department


class DepartmentApi(Resource):
    def get(self, id):
        try:
            department = read_one_department(id)
            return {"message": "Success", "department": department.to_dict()}
        except DepartmentNotFound:
            return {"message": "Department not found"}

    def put(self, id):
        data_json = request.get_json(force=True)
        department_schema = DepartmentSchema()
        try:
            department_data = department_schema.load(data_json)
            department = update_department(id, **department_data)
            return {"message": "Success", "department": department.to_dict()}
        except DepartmentNotFound:
            return {"message": "Department not found"}

    def delete(self, id):
        try:
            department = delete_department(id)
            return {"message": "Success", "department": department.to_dict()}
        except DepartmentNotFound:
            return {"message": "Department not found"}


class DepartmentListApi(Resource):
    def get(self):
        try:
            departments = read_departments()
            return {"message": "Success", "departments": [department.to_dict() for department in departments]}
        except DepartmentNotFound:
            return {"message": "Department not found"}

    def post(self):
        department_schema = DepartmentSchema()
        data_json = request.get_json(force=True)
        if data_json:
            data = department_schema.load(data_json)
            department = create_department(**data)
            return {"message": "Success", "department": department.to_dict()}
        return {"message": "Please, input data for department"}