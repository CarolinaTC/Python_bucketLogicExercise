class Product:

    """

    """
    def __init__(self,name_prod, qnt_prod):
        self.name_prod = name_prod
        self.qnt_prod = qnt_prod

    def __str__(self):
        return "{} {}".format(self.name_prod, self.qnt_prod)


    #TODO: obter o preco de cada produto consoante a quantidade comprada
    """
    Soup – €0.65 per tin
    Bread – €0.80 per loaf
    Milk – €1.30 per bottle
    Apples – €1.00 per bag 
    
    DESCONTOS:
    Current special offers are:
    Apples have 10% off their normal price this week
    Buy 2 tins of soup and get a loaf of bread for half price
    """