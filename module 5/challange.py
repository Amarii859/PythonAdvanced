
total =0


for number in range(1,11):

    if number % 2 ==0:
        total += number

print("The sum of even numbers from 1 to 10 is:" , total)


def greet_person(name) :

    print("hello" , name)

greet_person("alice")



def greed(name):

    message  = f"hello , {name}!"


    print(message)

greed("alice")

greeting = "hello"

def greet(name) :
    message = f"hello , {name}!"
    name("bob")

print(greet)

greeting = "hello"

def greet(name):

    global message

    message = f"{greeting},{name}"
    print(message)

greet("bob")
print("message")

greeting = "hello"
name="bob"


def greet():

    global greeting
    greeting = "goodbye"


    name = "alice"

    message = f"{greeting}, {name}"
    print(message)



greet()

print(greeting)

print(name)


def greet_person(name,greeting="hello"):

    message=f"{greeting} , {name}"

    return message

default_greeting = greet_person("alice")

custom_greeting = greet_person("bob0" , "hi")

print(default_greeting)
print(custom_greeting)
