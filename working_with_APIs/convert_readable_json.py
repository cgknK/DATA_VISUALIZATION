import json

filename = 'rate_limit.json'
with open(filename) as f:
    temp = json.load(f)

with open('readable_' + filename, 'w') as f:
    json.dump(temp, f, indent=4)