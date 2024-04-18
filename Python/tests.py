import unittest
import mergeSort as MS
import random

class TestMergeSort(unittest.TestCase):

    def test_sort(self):
        testArr = [
            {"pokemon":"Test","price":10.00},
            {"pokemon":"Test","price":100.00},
            {"pokemon":"Test","price":1000.00},
            {"pokemon":"Test","price":1000.00},
            {"pokemon":"Test","price":10000.00},
            {"pokemon":"Test","price":10000.00},
            {"pokemon":"Test","price":10001.00},
            {"pokemon":"Test","price":100011.00},
            {"pokemon":"Test","price":100011.00},
            {"pokemon":"Test","price":1000111.00}
        ]
        pokeMonArr = []
        for item in testArr:
            pokeMonArr.append(MS.Pokemon(item["pokemon"], item["price"]))
        testShuffled = pokeMonArr.copy()

        random.shuffle(testShuffled)
        MS.mergeSort(testShuffled, 0, len(testShuffled) - 1)

        for i in range(len(pokeMonArr)):
            self.assertEqual(pokeMonArr[i].price, testShuffled[i].price)


if __name__ == '__main__':
    unittest.main()
