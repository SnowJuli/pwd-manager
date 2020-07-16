from pymongo import MongoClient
from PyInquirer import prompt
import yaml

def addLogin():
    with open('config.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    # address = data[0]
    # TODO: Yaml isn't working
    client = MongoClient("") # Enter your address in the config.yaml File
    db = client["passwords"]
    dbcol = db["pwd"]

    addinfo = [
        {
            'type': 'input',
            'name': 'name',
            'message': 'Your Username: ',
        },
        {
            'type': 'input',
            'name': 'password',
            'message': 'Your Username: ',
        },
        {
            'type': 'input',
            'name': 'tag',
            'message': 'Provide a Name for the Informations: ',
        }
    ]
    options = prompt(addinfo)

    input_dict = {
        "username": options["name"],
        "password": options["password"],
        "tag": options["tag"]
    }
    info = dbcol.insert_one(input_dict)

    print(info.inserted_id)
