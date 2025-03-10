d={}
d[1] = d.get(1, 0) - 1 #means return 0 if not found and decrease it as 1
d['a'] = d.get('a', 0) + 1  #means return 0 if not found and increase it as 1

a={"name":"saif", "age":23,"wife":["Sss","sssssss",23],"b":2}
print(a)
# dictionary dont have Index
print(a["name"])
print(a.get("phone_number","not found"))
a["name"]="reyad"
print(a)
print("*********")
a.update({"name":"islam", "age":40,"wife":["ssss","sssssss",23]})
print(a)
del a["b"]
print(a)
print("*********")
a.pop("wife")
print(a)
a.popitem() #deletes last item
a.clear() #deletes all
x={"name":"saif", "age":23,"wife":["Sss","sssssss",23],"b":2}
print(x.keys())
print(x.values())
#how to append?
x["app"]="hello"
print(x)




# registration system
d={}
for i in range(int(input)):
    name = input()
    if name not in d:
        d[name] = 0
        print("OK")
    else:
        d[name] += 1
        print(name + str(d[name]))

ans = ""
for key, value in d.items():
    if value > 1:
        ans += (str(key) + " ") * value
