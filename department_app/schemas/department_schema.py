from department_app import ma

from department_app.models.department import Department


class DepartmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Department
        include_relationships = True
