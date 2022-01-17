from Bucket import  Bucket


def calc_subtotal(bucket, list_prods):
    """
    Subtotal calculation.
    :param bucket: bucket with the products chosen by the user
    :type bucket: Bucket
    :param list_prods: list of products available this week
    :type list_prods: list of str
    :return: the subtotal value
    """

    subtotal = 0

    for product in bucket.get_products().keys():
        subtotal = subtotal + bucket.get_products()[product] * list_prods[product]

    return subtotal

######## Discounts ###############

def calc_apples_discount(bucket, list_prods):
    """
    Calculation of the apples discount.

    :param bucket: bucket with the products chosen by the user
    :type bucket: Bucket
    :param list_prods: list of products available this week
    :type list_prods: list of str
    :return:  the value of discount to made in the apples purchase
    """

    apples_discount = bucket.get_qnt_of_product('Apples') * list_prods['Apples'] * 0.1
    return round(apples_discount, 2)

def calc_bread_discount(bucket, list_prods):
    """
    Calculation of the bread discount.

    :param bucket: bucket with the products chosen by the user
    :type bucket: Bucket
    :param list_prods: list of products available this week
    :type list_prods: list of str
    :return the value of bread discount to apply on purchase
    """

    bread_discount = 0
    number_bread_discounts = 0

    if bucket.get_qnt_of_product('Soup') >= 2:
        number_bread_discounts = bucket.get_qnt_of_product('Soup') // 2

    if number_bread_discounts >= bucket.get_qnt_of_product('Bread'):
        bread_discount = bread_discount + bucket.get_qnt_of_product('Bread') * list_prods['Bread'] * 0.5 # all breads tem descontos
    else:
        bread_discount = bread_discount + number_bread_discounts * list_prods['Bread'] * 0.5 # menos descontos do que paes, portanto so aplico os descontos que tiver

    return bread_discount

def calc_discount(bucket, list_prods):
    """
    Calculation the value of total of discount to apply om purchase.

    :param bucket: bucket with the products chosen by the user
    :type bucket: Bucket
    :param list_prods: list of products available this week
    :type list_prods: list of str
    :return: value of total discount to apply on purchase
    """


    discount = 0

    if bucket.has_product('Apples'):
        discount = discount + calc_apples_discount(bucket, list_prods)

    if bucket.has_product('Soup') and bucket.has_product('Bread'):
        discount = discount + calc_bread_discount(bucket, list_prods)

    return discount


