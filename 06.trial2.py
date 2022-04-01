mydict = {"name": "Max","age":29,"city":"New York"}
mydict_2 = dict(name="Raj",height=175,color="brown")
# # if "name" in mydict:
# #     print(mydict["name"])
# for key in mydict.keys():
#     print(key)
mydict.update(mydict_2)
print(mydict)