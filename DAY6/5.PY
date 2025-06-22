# GENERATORS

#ex=>1
def gen_demo():
    yield "first statement"
    yield "second statement"
    yield "third statement"

gen = gen_demo()  # here object defined.
for i in gen:
    print(i)  # function call loop mai jana ka bad hoga.

# Function Behavior:
# return: Terminates the function completely and returns a single value
# yield: Pauses the function, saves its state, and returns a value (can resume later)

# Memory Usage:
# return: Returns all data at once (may use more memory)
# yield: Generates values one at a time (memory efficient)


#ex 2
def square(num):
    for i in range(i,num+1):
        yield i**2

gen = square(10)
print(next(gen))
print(next(gen))
print(next(gen))

for i in gen:
    print(i)

# def square(num):
#     for i in range(i,num+1):
#         return i**2
# 