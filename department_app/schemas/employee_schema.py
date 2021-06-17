from department_app import ma

from department_app.models.employee import Employee


class EmployeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Employee
        include_relationships = True
