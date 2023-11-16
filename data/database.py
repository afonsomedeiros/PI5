from hashlib import md5
from passlib.hash import pbkdf2_sha512 as hsh
from pymongo.collection import Collection
from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib import parse
from datetime import datetime
from json import dumps
from bson import json_util


def get_uri():
    return f"mongodb+srv://afonso2k:{parse.quote('leticia@2014')}@cluster0.r0cmo.mongodb.net/?retryWrites=true&w=majority"


def get_database(client: MongoClient, databasename):
    return client[databasename]


def get_client(uri):
    return MongoClient(get_uri(), server_api=ServerApi('1'))


def get_user(_id):
    uri = get_uri()
    client = get_client(uri)
    db = get_database(client, "PIV")
    return db.users.find_one({'_id': ObjectId(_id)})


def get_user_email(email):
    uri = get_uri()
    client = get_client(uri)
    db = get_database(client, "PIV")
    return db.users.find_one({'email': email})


def get_admeasurement_interval(variable_id = 0, start=None, end=None):
    uri = get_uri()
    client = get_client(uri)
    db = get_database(client, "PIV")
    query = "{"
    if int(variable_id) > 0:
        query += f"\"variable_id\":{variable_id}"
    if start or end:
        if 'variable_id' in query:
            query += ", "
        query += "\"date\": {"
        if start:
            query += f"\"$gte\": \"{start}\""
        if end:
            if '$gte' in query:
                query += f", "
            query += f"\"$lt\": \"{end}\""
        query += "}"
    query += "}"
    json = json_util.loads(query)
    return db.admeasurement.find(json)
    


    json = json_util.dumps(query)
    return db.admeasurement.find(query)

def gen_hash(password, secret: str):
    _secret = md5(secret.encode()).hexdigest()
    _password = md5(password.encode()).hexdigest()
    return hsh.hash(_secret+_password)


def verify(password, user_password, secret):
    _secret = md5(secret.encode()).hexdigest()
    _password = md5(password.encode()).hexdigest()
    return hsh.verify(_secret+_password, user_password)


def insert_user(name, email, password):
    uri = get_uri()
    client = get_client(uri)
    db = get_database(client, "PIV")
    _password = gen_hash(password, "")
    user = {
        'name': name,
        'email': email,
        'password': password
    }
    inserted_id = db.users.insert_one(user).inserted_id
    return inserted_id


def insert_admeasurement(variable_id, value, date):
    uri = get_uri()
    client = get_client(uri)
    db = get_database(client, "PIV")
    admeasurement = {
        'variable_id': variable_id,
        'value': value,
        'date': date
    }
    inserted_id = db.admeasurement.insert_one(admeasurement).inserted_id
    return inserted_id

