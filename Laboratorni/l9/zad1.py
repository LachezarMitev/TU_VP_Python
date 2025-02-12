import json

gIgnatov = {
    "fname": "Georgi",
    "lname": "Ignatov",
    "age": 49,
    "boss": True
}

johnson = json.dumps(gIgnatov, indent=5)
print(johnson)