# def say_hello(name):
#     print('Hello, {}'.format(name))
#     say_hello(name)

# say_hello('Elaine')

# def countdown(num):
#     #base case
#     if num == 0:
#         print('Blast off!')
#         return
#     # recursive step
#     print(num)
#     countdown(num-1)

# countdown(10)

# handles edge case for negative number

def countdown(num):
    #base case
    if num == 0:
        print('Blast off!')
        return
    elif num < 0:
        print('Please add a positive number')
        return
    # recursive step
    print(num)
    countdown(num-1)

# countdown(20)
# countdown(-2)

numbers = [1, 1, 1, 1, 1]

def add_number(numbers_array, result=0):
    # base case
    num = numbers_array.pop()
    result += num
    if len(numbers_array) == 0:
        return result
    return add_number(numbers_array, result)

print(add_number(numbers))