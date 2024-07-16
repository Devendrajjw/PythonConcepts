import pytest

from demo4.sample import DatabaseConnection

@pytest.fixture
def sample_data():
    def createdata(a,b):
       return {"a":a,"b":b}
    return createdata


@pytest.fixture(scope= "function")
def db_connection():
    # Setup: Create and connect the database
    db = DatabaseConnection()
    db.connect()
    yield db
    # Teardown: Disconnect the database
    db.disconnect()
