from pathlib import Path
import json

def get_new_user():
    """gathers user info and writes it to a file"""
    path = Path("user_info.json")
    contents = {}
    username = input("What is your name? ")
    age = input("How old are you? ")
    location = input("What city do you live in? ")
    contents["username"] = username
    contents["age"] = age
    contents["location"] = location
    contents_json = json.dumps(contents)
    path.write_text(contents_json)
    print(f"We'll remember you next time, {username}!")

def greet_user():
    """Greet user by name if they've used program before
    and tells them about themselves. If not, gathers the 
    info and writes it to a file"""
    path = Path("user_info.json")
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        user_name = user_info["username"]
        user_age = user_info["age"]
        user_location = user_info["location"]
        current_user = input("Please confirm your username: ")
        if current_user == user_name:
            print(f"Welcome back, {user_name.title()}, you are {user_age} years old and from {user_location.title()}")
        else:
            print("Invalid, please make a new user.")
            get_new_user()
        

greet_user()