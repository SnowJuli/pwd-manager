# This is a test file for the Workflow
# It is used to show if the MongoDB is correctly installed

from pymongo import MongoClient
import yaml

# Loading the Address
with open("config.yaml") as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

# Config
address = data["location"]
client = MongoClient(address)
db = client["passwords"]
dbcol = db["pwd"]

# Example inforations
name = "tester"
password = "secretpassword"
tag = "testing"


input_dict = {
    "username": name,
    "password": password,
    "tag": tag,
}
# Inserting the informations
info = dbcol.insert_one(input_dict)
