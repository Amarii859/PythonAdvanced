fruits = {
    "apple": 5 ,
    "banana": 7,
    "orange": 3
}

try:
    print(fruits["cherry"])
except KeyError:
    print("The key does not exist")