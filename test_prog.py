import unittest
import projectLib
from Bucket import Bucket

AVALILABLE_WEEK_PRODUCTS_AND_PRICE = {
                                'Apples' : 1.00,
                                'Soup': 0.65,
                                'Milk': 1.30,
                                'Bread': 0.80}



class TestProg(unittest.TestCase):

    def test_add_product(self):
        bucket = Bucket()

        self.assertEqual(len(bucket.products), 0)

        bucket.add_product('Pear')

        self.assertEqual(len(bucket.products), 1)

        self.assertEqual(bucket.products['Pear'], 1)

        bucket.add_product('Pear')

        # adds 1 to the quantity and not an extra entry in the dictionary
        self.assertEqual(len(bucket.products), 1)
        self.assertEqual(bucket.products['Pear'], 2)

        bucket.add_product('Apple')

        self.assertEqual(len(bucket.products), 2)
        self.assertEqual(bucket.products['Apple'], 1)

    def test_has_product(self):
        bucket = Bucket()

        result = bucket.has_product('Pear')  # TODO : ???????
        self.assertFalse(result)

        bucket.products['Pear'] = 1
        result = bucket.has_product('Pear')
        self.assertTrue(result)

    def test_empty_bucket(self):
        bucket = Bucket()

        self.assertTrue(bucket.empty_bucket())

        bucket.products['Pear'] = 1

        self.assertFalse(bucket.empty_bucket())

    def test_get_products(self):
        bucket = Bucket()

        self.assertEqual(bucket.get_products(), {})

        bucket.products['Pear'] = 1
        bucket.products['Apple'] = 1

        products = bucket.get_products()

        self.assertTrue('Pear' in products.keys())
        self.assertTrue('Apple' in products.keys())
        self.assertFalse('Pineapple' in products.keys())

    def test_get_qnt_of_product(self):

        bucket = Bucket()

        bucket.products['Apple'] = 1

        self.assertEqual(bucket.get_qnt_of_product('Apple'), 1)

        bucket.products['Apple'] = 2

        self.assertEqual(bucket.get_qnt_of_product('Apple'), 2)

    def test_calc_subtotal(self):

        # TODO: mock when get_products return x

        bucket = Bucket()

        bucket.products['Apples'] = 1
        bucket.products['Milk'] = 2
        bucket.products['Soup'] = 3
        bucket.products['Bread'] = 4

        self.assertEqual(projectLib.calc_subtotal(bucket, AVALILABLE_WEEK_PRODUCTS_AND_PRICE), 8.75)

    def test_calc_discount(self):
        bucket = Bucket()

        bucket.products['Apples'] = 1
        bucket.products['Milk'] = 2
        bucket.products['Soup'] = 3
        bucket.products['Bread'] = 4

        self.assertEqual(projectLib.calc_discount(bucket, AVALILABLE_WEEK_PRODUCTS_AND_PRICE), 0.5)

    def test_calc_apple_discount(self):
        bucket = Bucket()

        bucket.products['Apples'] = 1

        self.assertEqual(projectLib.calc_apples_discount(bucket, AVALILABLE_WEEK_PRODUCTS_AND_PRICE), 0.1)

        bucket.products['Apples'] = 3
        self.assertEqual(projectLib.calc_apples_discount(bucket, AVALILABLE_WEEK_PRODUCTS_AND_PRICE), 0.3)



    def test_calc_bread_discount(self):

        bucket = Bucket()
        # calc breads = soups
        bucket.products['Soup'] = 2
        bucket.products['Bread'] = 2

        self.assertEqual(projectLib.calc_bread_discount(bucket, AVALILABLE_WEEK_PRODUCTS_AND_PRICE), 0.4)

        bucket = Bucket()

        # calc breads > soups
        bucket.products['Soup'] = 2
        bucket.products['Bread'] = 4

        self.assertEqual(projectLib.calc_bread_discount(bucket, AVALILABLE_WEEK_PRODUCTS_AND_PRICE), 0.4)


        bucket = Bucket()

        # calc breads < soups
        bucket.products['Soup'] = 6
        bucket.products['Bread'] = 2

        self.assertEqual(projectLib.calc_bread_discount(bucket, AVALILABLE_WEEK_PRODUCTS_AND_PRICE), 0.8)


if __name__ == '__main__':
    unittest.main()







