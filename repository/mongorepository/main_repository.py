import pymongo
from passlib.hash import pbkdf2_sha256 as sha256
from config.config import APP_CONFIG

client = \
    pymongo.MongoClient(APP_CONFIG['MONGO_URL'])

db = client.coppel

new_user = {
    "name": "Marco",
    "age": "27",
    "email": "noexiste@hotmail.com.crazy",
    "password": "123456",
}

# db.users.insert_one(new_user)

# print(db.users.find_one())


def store_user(user):
    db.users.insert_one(user)


def get_user(email):
    print(email)
    return db.users.find_one({"email": email})


def verify_password(password, hash):
    return sha256.verify(password, hash)


def generate_hash(password):
    return sha256.hash(password)


