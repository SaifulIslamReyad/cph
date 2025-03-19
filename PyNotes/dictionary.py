from icecream import ic


d={}
d['a'] = d.get('a', 0) + 1  #means return 0 if not found and increase it as 1
d[1] = d.get(1, 0) - 1 #means return 0 if not found and decrease it as 1

a={"name":"saif", "age":23,"b":2}
ic(a)
# dictionary dont have Index
ic(a["name"])
ic(a.get("phone_number","not found"))
a["name"]="reyad"
ic(a)

a.update({"name":"islam", "age":40,"father":["kamal","7-10-71",50]})
ic(a)
del a["b"]
ic(a)

a.pop("father")
ic(a)
a.popitem() #deletes last item
a.clear() #deletes all
x={"name":"saif", "age":23,"father":["Kamal","7-10-71",50],"b":2}
ic(x.keys())
ic(x.values())
#how to append?
x["app"]="hello"
ic(x)




# registration system
d={}
for i in range(int(input)):
    name = input()
    if name not in d:
        d[name] = 0
        ic("OK")
    else:
        d[name] += 1
        ic(name + str(d[name]))

ans = ""
for key, value in d.items():
    if value > 1:
        ans += (str(key) + " ") * value
