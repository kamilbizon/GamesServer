import json

ziemniak = [2, 1, 3, 7]

ziemniakZestringowany = json.dumps(ziemniak)

print(ziemniakZestringowany, ziemniak)

nowyziemniak = json.loads(ziemniakZestringowany)
print(type(nowyziemniak))