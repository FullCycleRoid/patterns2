import json

class TextFile:
    def __init__(self, content):
        self.content = content

    def read(self):
        return f"Reading text file: {self.content}"


class JsonFile:
    def __init__(self, data):
        self.data = data

    def parse(self):
        return json.dumps(self.data)


class JsonFileAdapter:
    def __init__(self, json_file):
        self.json_file = json_file

    def read(self):
        return f"Reading JSON file: {self.json_file.parse()}"


text_file = TextFile("Hello, this is a plain text file.")
json_file = JsonFile({"name": "John", "age": 30})

json_adapter = JsonFileAdapter(json_file)


print(text_file.read())
print(json_adapter.read())