import os
import tempfile

import pytest

import wsgi


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create a temporary file to isolate the database for each test
    db_fd, db_path = tempfile.mkstemp()
    # create the app with common test config
    wsgi.app.config["TESTING"] = True
    wsgi.app.config["DATABASE"] = db_path

    # create the database and load test data
    with wsgi.app.test_client() as client:
        with wsgi.app.app_context():
            wsgi.db.init_all()
        yield client

    os.close(db_fd)
    os.unlink(wsgi.app.config['DATABASE'])
    yield app

    # close and remove the temporary database
    os.close(db_fd)
    os.unlink(db_path)