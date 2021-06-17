from . import app, db

from flask import render_template, redirect

from .models.department import Department


@app.route("/departments")
def departments():
    return render_template("departments.html", data={"departments":db.session.query(Department).all(),
                                                     "title": "Departments"})


@app.route('/department/<int:department_id>')
def department(department_id):
    return render_template("department.html", data={"department": db.session.query(Department).get(department_id),
                                                    "title": "Department"})