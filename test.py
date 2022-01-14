import sys

from Bucket import Bucket

print('Number of arguments: {}'.format(len(sys.argv)))
print('Argument(s) passed: {}'.format(str(sys.argv)))

productList = sys.argv[1:None]

print('Product(s): {}'.format(str(productList)))

AVALILABLE_WEEK_PRODUCTS = {'Apples', 'Soup', 'Batatas'}

bucket = Bucket()

for product in productList:

    if product in AVALILABLE_WEEK_PRODUCTS:
        ola = "batatas"
        # bucket.add_prod(product)
    else:
        print('This product is not available this week: {}'.format(product))
        exit()




