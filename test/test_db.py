from config.config import APP_CONFIG
from repository.mongorepository.main_repository import db
# run this inside the docker container or set up a .env file
# very basic test for now, not a lot of time,
# objective test the main features on this service
# i dont need test jwt or framework because they are tested already
# * db string setup
# * db conection


def test_mongo_connection_string():
    assert APP_CONFIG["MONGO_URL"] is not None


def test_db_connection():
    assert db is not None
