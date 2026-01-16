# This script ensures a unique index on the email field in the users collection
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['octofit_db']
users = db['octofit_tracker_user']
users.create_index([('email', 1)], unique=True)
print('Unique index on email ensured for users collection.')
