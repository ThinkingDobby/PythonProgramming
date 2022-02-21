import json

user = {
    "id":"gildong",
    "password":"198123",
    "age":30,
    "hobby":["football", "programming"]
}

json_data = json.dumps(user)
print(json_data)
print(type(user))
print(type(json_data))