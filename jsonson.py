import json
data1={
    'no' : 1,
    'name': 'Penis',
    'url': 'httl://www.pipi.us'
}
json_str = json.dumps(data1)
print("Python primary data: ",repr(data1))
print("JSON Obejct: ",json_str)
data2 = json.loads(json_str)
print("data2['name']:",data2['name'])
print("data2['url']:", data2['url'])

