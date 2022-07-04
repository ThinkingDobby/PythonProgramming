import json

user = {
    "id":"gildong",
    "password":"198123",
    "age":30,
    "hobby":["football", "programming"]
}

json_data = json.dumps(user)

data = json.loads(json_data)
print(data)
print(type(data))