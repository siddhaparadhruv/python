from turtle import update


mydict ={
    "viken":"my name is ",
    "pareshbhae": "my father name is ",
    "viken2" : [1,2,3,4,5,6,7,8,9 ],
    "lakkad": {"viken":"lakkad"},
    1 :  2,
 }
# print (type(mydict.keys()))
# print (list (mydict.keys()))
# print (mydict.values())
# print (list (mydict.values  ()))
# print (mydict.items())
updateDict = {
    "viken3": "plary of circet "
}
mydict.update(updateDict)
print (mydict.get ("viken3"))
print (mydict.get ("viken2"))
print (mydict.get ("viken"))
# print (mydict)
