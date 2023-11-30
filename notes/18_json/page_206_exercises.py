from pathlib import Path
import json

def fave_number():
    """remembers a users favourite number"""
    path = Path("fave_number.json")
    if path.exists():
        contents = path.read_text(encoding="utf-8")
        print(f"I know your favourite number! It's {contents}")
    else:
        number = input("What's your favourite number? ")
        path.write_text(number)

fave_number()