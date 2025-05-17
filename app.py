print('Hello World!')
print('*' * 10)

# variables
sutents_count = 1000
rating = 4.99
is_published = False
course_name = "Python \"Programming\" for Beginners"
print(len(course_name))
print(course_name[0])
print(course_name[-1])
print(course_name[0:3])
print(course_name[0:])
print(course_name[:3])
print(course_name[:])

# string methods
first = 'John'
last = 'Smith'
full_name = f"{first} {last}"
print(full_name.upper())

# # while loop
# command = ""
# while command != 'quit':
#     command = input(">")
#     print("ECHO", command)

# for loop
for number in range(1, 10):
    if number % 2 == 0:
        print(number)

# functions


# def greet_user(firstname, lastname):
#     print(f"Hi {firstname}, {lastname}")
#     print("Welcome aboard!")


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("John")
print(message)
