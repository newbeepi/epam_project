from wtforms import StringField, DateField, FloatField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms.validators import ValidationError

from department_app.models.department import Department
from . import db


def check_department_exists(form, field):
    departments = db.session.query(Department).all()
    if field.data in departments:
        raise ValidationError('department exists')


def check_department_not_exists(form, field):
    departments = db.session.query(Department).all()
    if field.data not in departments:
        raise ValidationError('department not exists')


class DepartmentForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), check_department_exists()])


class EmployeeForm(FlaskForm):
    name = StringField('name', validators=DataRequired)
    surname = StringField('surname', validators=DataRequired)
    date_of_birth = DateField('date_of_birth', validators=DataRequired)
    salary = FloatField('salary')
    department = StringField('department', validators=[DataRequired(), check_department_not_exists()])