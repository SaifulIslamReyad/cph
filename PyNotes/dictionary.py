from icecream import ic
from collections import defaultdict


# ==================== BASIC DICTIONARY OPERATIONS ====================
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


# ==================== DEFAULTDICT IMPLEMENTATION ====================

# 1. Basic defaultdict with int (most common)
count_dict = defaultdict(int)  # default value is 0
count_dict['a'] += 1  # No need to check if key exists!
count_dict['b'] += 5
count_dict['a'] += 2
ic("Count dict:", dict(count_dict))  # {'a': 3, 'b': 5}

# 2. defaultdict with list (for grouping)
group_dict = defaultdict(list)
group_dict['fruits'].append('apple')
group_dict['fruits'].append('banana')
group_dict['vegetables'].append('carrot')
ic("Group dict:", dict(group_dict))

# 3. defaultdict with set (for unique items)
unique_dict = defaultdict(set)
unique_dict['colors'].add('red')
unique_dict['colors'].add('blue')
unique_dict['colors'].add('red')  # duplicate, won't be added
ic("Unique dict:", dict(unique_dict))

# 4. defaultdict with custom function
def default_value():
    return "Not Found"

custom_dict = defaultdict(default_value)
custom_dict['existing'] = "Found"
ic("Custom dict existing:", custom_dict['existing'])
ic("Custom dict missing:", custom_dict['missing'])

# 5. defaultdict with lambda for complex defaults
nested_dict = defaultdict(lambda: defaultdict(int))
nested_dict['user1']['score'] += 10
nested_dict['user1']['level'] += 1
nested_dict['user2']['score'] += 5
ic("Nested dict:", dict(nested_dict))

# 6. Practical example: Word frequency counter
text = "hello world hello python world"
word_freq = defaultdict(int)
for word in text.split():
    word_freq[word] += 1
ic("Word frequency:", dict(word_freq))

# 7. Practical example: Grouping by first letter
names = ['alice', 'bob', 'charlie', 'david', 'eve', 'alex']
grouped_names = defaultdict(list)
for name in names:
    grouped_names[name[0]].append(name)
ic("Grouped names:", dict(grouped_names))

# 8. Converting back to regular dict
regular_dict = dict(count_dict)
ic("Converted to regular dict:", regular_dict)

# 9. Comparison: Regular dict vs defaultdict
print("\n=== COMPARISON ===")
# Regular dict - need to check key existence
regular = {}
if 'key' not in regular:
    regular['key'] = []
regular['key'].append('value')

# defaultdict - no need to check
default = defaultdict(list)
default['key'].append('value')
ic("Both methods result in:", regular, dict(default))

# ==================== ADVANCED DEFAULTDICT PATTERNS ====================

# 10. defaultdict for graph representation
graph = defaultdict(list)
edges = [(1, 2), (1, 3), (2, 4), (3, 4)]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)  # undirected graph
ic("Graph representation:", dict(graph))

# 11. defaultdict for counting with conditions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_odd_count = defaultdict(int)
for num in numbers:
    if num % 2 == 0:
        even_odd_count['even'] += 1
    else:
        even_odd_count['odd'] += 1
ic("Even/Odd count:", dict(even_odd_count))

# 12. defaultdict for matrix operations
matrix_dict = defaultdict(lambda: defaultdict(float))
matrix_dict[0][0] = 1.5
matrix_dict[1][2] = 2.3
ic("Matrix dict:", dict(matrix_dict))


# ==================== ORIGINAL CODE ====================




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
