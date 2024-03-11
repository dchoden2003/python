fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)

fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)
    if x =="banana":
        break # cont checking till banana.

fruits = ["apple","banana","cherry"]
for x in fruits:
    if x =="banana":
        continue
    print(x) # starts the loop again and goes to cherry.
    

for x in range(6):
    print(x)# print till 5

for x in range(2,6):
    print(x) # print till 2 to 5.

for x in range(2,30,2): # no.goes till 2 to 30.addint 2 to every number.
    print(x) 

for x in range(6):
    print(x)
else:
    print("finished")

