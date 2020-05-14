# def factorial(num):
#     result = 1
#     for data in range(1, num+1):
#         result = result*data
#     return result



def factorial(num):
    if num == 1:
        return 1
    return factorial(num-1)*num
print(factorial(5))