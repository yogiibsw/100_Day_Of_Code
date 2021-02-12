import json
  # Key:value mapping
student = {
       "Name": "Naruto",
        "Roll_no": "5444674",
        "Grade": "A",
        "Age": 25,
       }

with open("data1.json", "w") as write_file:
    json.dump(student, write_file)

with open("data1.json", "r") as read_file:
    b = json.load(read_file)
    print(b)
