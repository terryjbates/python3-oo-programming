import unittest
from typedlist import TypedList

class TestTypedList(unittest.TestCase):
    def setUp(self):
        self.aTypedList = TypedList(1,[1,2,3])

    def testGetItem(self):
        self.assertEqual(self.aTypedList[1], 2)

    def testSetItem(self):
        self.aTypedList[1] = 3
        self.assertEqual(self.aTypedList[1], 3)

if __name__ == '__main__':
    unittest.main()

