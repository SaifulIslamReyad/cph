# name="saiful islam reyad"
# #name='saiful islam reyad' also correct
# #name='''saiful islam reyad''' also correct
# #name = "saiful \"Islam reyad" also correct while using a " in the midddle
# name2= "Sakib\n Al\b h\tas\\nan"
# print( name,name2)
name3='''helllllllllo
i am saif'''

print(name3.replace("helllllllllo","hlw"))
print(name3.replace("h","b"))
print(name3.replace("l","x",2))
print(name3.upper())
name3=name3.lower()
print(name3)
name3=name3.capitalize()
print(name3)
print(name3.swapcase())
print(name3.strip("H"))
#can remove only first or last letter
print(name3.count("l"))
print(name3.count("ll"))
print("+".join(name3))
print(" ".join(name3))
nam= "+".join([name3,"Reyad"])
print(nam)
print(len(nam))

