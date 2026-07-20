import json
from pathlib import Path


class JsonStore:
    def save(self, filename: str, data: dict):
        path = Path(filename)
        
        with open(path, "w") as file:
            json.dump(data, file, indent=4)

    def load(self, filename: str):
        path = Path(filename)

        if not path.exists():
            return {}

        with open(path, "r") as file:
            return json.load(file)