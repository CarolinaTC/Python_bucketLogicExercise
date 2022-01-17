"""
Carolina Carrilho
May 2021
"""

import sys
import projectLib
from Bucket import Bucket



productList = sys.argv[1:None]

print('Price Basket: {}'.format(str(productList)))


AVALILABLE_WEEK_PRODUCTS_AND_PRICE = {
                                'Apples' : 1.00,
                                'Soup': 0.65,
                                'Milk': 1.30,
                                'Bread': 0.80}

bucket = Bucket()



# check that the product is on the list of products available for sale.
for product in productList:

    if product in AVALILABLE_WEEK_PRODUCTS_AND_PRICE:
        bucket.add_product(product)


    else:
        print('This product is not available this week: {}'.format(product))
        exit()

if bucket.empty_bucket():
    print('Your bucket is empty. Choose at least 1 product of the list.{}'.format(AVALILABLE_WEEK_PRODUCTS_AND_PRICE))

subtotal = projectLib.calc_subtotal(bucket, AVALILABLE_WEEK_PRODUCTS_AND_PRICE)
discount = projectLib.calc_discount(bucket, AVALILABLE_WEEK_PRODUCTS_AND_PRICE)
total = round(subtotal - discount,2)

print('Subtotal: {}'.format(subtotal))
print('Discount: {}'.format(discount))
print('Total: {}'.format(total))




