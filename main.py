from PyInquirer import prompt

from src.add import addLogin
from src.remove import removeLogin
from src.list import listLogin
from src.pwd import configurePwd

questions = [
    {
        "type": "list",
        "name": "action",
        "message": "What do you want to do? ",
        "choices": [
            {"key": "a", "name": "Add a Login Information", "value": "add"},
            {"key": "r", "name": "Remove a Information ", "value": "remove"},
            {"key": "l", "name": "Search for a Information", "value": "list"},
            {"key": "c", "name": "Configure the master password", "value": "pwd"},
            {"key": "q", "name": "Quit", "value": "quit"},
        ],
    }
]

if __name__ == "__main__":
    answers = prompt(questions)
    action = answers["action"]

    if action == "add":
        addLogin()
    elif action == "remove":
        removeLogin()
    elif action == "list":
        listLogin()
    elif action == "pwd":
        configurePwd()
    elif action == "quit":
        pass
