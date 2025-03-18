'''
define a function
that takes two arguments
and returns their sum, product and difference
as a tuple
'''

def calculate_sum_product_difference(num1, num2):
    sum = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    return sum, difference, product

print(calculate_sum_product_difference(1,2))


# using lambda function
sum = lambda x,y: x + y
difference = lambda x,y: x - y


def calculate_sum(numi, num2, *numbers):
    sum = numi + num2
    for num in numbers:
        sum += num
    return sum
print(calculate_sum (1, 2))



def difference(num1 , num2 , *number):
    sum = num1 + num2
    for num in number : 
        sum += num
    return sum
diff = difference(7, 10, *[1 , 2, 3 ,4 ,5])
print(diff)


