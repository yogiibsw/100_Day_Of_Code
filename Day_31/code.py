import json

with open('test.json', 'r') as f:
    json_text = f.read()

apod_dict = json.loads(json_text)
print(apod_dict['explanation'])

new_json_string = json.dumps(apod_dict, indent=4)
print(new_json_string)
