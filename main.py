



import unittest
from search import linear_search
from search import binary_search
class SearchTestCase(unittest.TestCase):
   def test_linear_search(self):
       values=[1,3,5,7,9,10,12]
       res= linear_search(values,5)
       self.assertEqual(res,2)
       self.assertEqual(linear_search(values,1),0)
       self.assertEqual(linear_search(values,12),6)
       self.assertEqual(linear_search(values,6),-1)


   def test_binary_search(self):
       values=[1,3,5,7,9,10,12]
       res=binary_search(values,10)
       self.assertEqual(res, 5)
       self.assertEqual(linear_search(values, 1), 0)
       self.assertEqual(linear_search(values, 12), 6)
       self.assertEqual(linear_search(values, 45), -1)


if __name__=='__main__':
   unittest.main()
