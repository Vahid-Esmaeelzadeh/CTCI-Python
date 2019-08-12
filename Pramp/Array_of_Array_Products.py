'''
Array of Array Products
Given an array of integers arr, you’re asked to calculate for each index i the product of all integers except the
integer at that index (i.e. except arr[i]). Implement a function arrayOfArrayProducts that takes an array of integers
and returns an array of the products.
'''

def calcProductArray(arr):
    n = len(arr)

    if n == 0 or n == 1:
        # no values to multiply if n equals to 0 or 1
        return []

    productArr = []
    product = 1

    for i in range(n):
        productArr.append(product)
        product *= arr[i]

    product = 1
    for i in range(n-1, -1, -1):
        productArr[i] *= product
        product *= arr[i]

    return productArr


a = [2, 3, 4 ,5]
print(calcProductArray(a))