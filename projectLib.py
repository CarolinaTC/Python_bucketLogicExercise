from Product import  Product



def add_register_prod(bucket):
    """
    add a register of a new product
    """
    name_prod = input("your product: ")
    qnt_prod = input("Quantity to be purchased: ")

    bucket.add_prod(name_prod, Product(name_prod, qnt_prod))
    print("product {} was registered.".format(name_prod))

def print_list_prod(bucket):
    """
    print all products registred
    """
    print(bucket.get_list_of_products())
