class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "postgresql://flask:flask_password@localhost/department"
    CSRF_ENABLED = True


