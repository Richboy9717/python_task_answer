import json
# x = (3,5,7,54,23)
# x_json = json.dumps(x)
# x2 = json.loads(x_json)
# print(x2)
#
# bemor = {
#   "ism": "Alijon Valiyev",
#   "yosh": 30,
#   "oila": True,
#   "farzandlar": ("Ahmad","Bonu"),
#   "allergiya": None,
#   "dorilar": [
#     {"nomi": "Analgin", "miqdori": 0.5},
#     {"nomi": "Panadol", "miqdori": 1.2}
#   ]
# }
#
# bemor_json = json.dumps(bemor,indent=4)
# print(bemor_json)
# bemor2 = json.loads(bemor_json)
#
# with open('bemor.json','w') as f:
#     json.dump(bemor_json,f)
#
# with open('bemor.json') as s:
#   bemorr = json.load(s)
# print(type(bemorr))
data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
d_json = json.dumps(data)

talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
talaba = json.loads(talaba_json)

with open('dat.json','w') as f:
  json.dump(data,f)

with open('tala.json','w') as f:
  json.dump(talaba,f)

st = 'students.json'
with open(st) as f:
  student = json.load(f)
student1,abz = student['student'][0],'\n'

for k,v in student1.items():
  print(k,'-',v)
print(abz)
student1 = student['student'][1]
for k,v in student1.items():
  print(k,'-',v)
print(abz)
student1 = student['student'][2]
for k,v in student1.items():
  print(k,'-',v)

# with open('api-result.json') as f:
#   wiki = json.load(f)
# print(wiki['query']['pages']['13801']['title'])
# print(wiki['query']['pages']['13801']['extract'])
