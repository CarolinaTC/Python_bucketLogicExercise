
class Bucket:
    """
    Object that is used to handle items purchase
    """

    def __init__(self):
        self.products = {} # dict nome produto(key) e qtnd prod (value)


    def add_prod(self, name_prod, prod):
        self.products[name_prod] = prod


    def get_list_of_products(self):

        items = self.products.keys()
        prod_list = []

        # order users by user_id (compare all ids in lower case to make sure that they are correctly ordered)
        for item in items:
            prod_list.append(item) #TODO: corrigir para printar um dict com o produto e a quantidade associada

        return prod_list

