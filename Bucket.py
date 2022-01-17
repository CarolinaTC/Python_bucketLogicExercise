
class Bucket:
    """
    Object that is used to handle items purchase.
    """

    def __init__(self):
        self.products = {} # dict nome produto(key) e qtnd prod (value)



    def has_product(self, name_prod):
        """
        Verify if the name of the product is in the bucket

        :param name_prod: name of the product to check
        :type name_prod: str
        :return: bool
        """

        if name_prod in self.products.keys():
            return True

    def empty_bucket(self):
        """
        Check if the bucket is empty. It is necessary at least one of the products available to proceed.

        :return: bool
        """

        if not self.products:
            return True
        else:
            return False


    def add_product(self, name_prod):
        """
        Add a product on bucket and increment the amount in case of this existence

        :param name_prod: name of the product added by user
        :type name_prod: str

        """

        if name_prod in self.products:

            self.products[name_prod] = self.products[name_prod] + 1

        else:
            self.products[name_prod] = 1


    def get_products(self):
        """
        Handle the products of the bucket

        """
        return self.products


    def get_qnt_of_product(self, name_prod):
        """
        get the amount of the 1 product that is in the bucket.

        :param name_prod: name of the product to count the amount
        :return: a int that means the amount of the product
        """

        if name_prod in self.products.keys():

            qnt_of_prod = self.products[name_prod]

            return qnt_of_prod







