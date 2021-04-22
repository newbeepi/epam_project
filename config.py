class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "postgresql://flask:flask_password@localhost/department"
    CSRF_ENABLED = True
    SECRET_KEY = "2j8J9dkJnd877n1hDdjjUwhd7163gFnxg2q9jamHD"


class TestConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    CSRF_ENABLED = True
    SECRET_KEY = "2j821Jd9dkJnd877n1hDdjjUwhd7163g2q9jamHD"