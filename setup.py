from setuptools import setup

setup(
    name='epam_project',
    version='0.0.1',
    packages=['rest', 'models', 'service', 'views'],
    install_requires=[
        'flask',
        'flask_restful',
        'flask_sqlalchemy',
        'importlib; python_version >= "3.8"',
    ],
)
