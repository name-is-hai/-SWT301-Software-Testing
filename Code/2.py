import unittest
  
def min2(num1, num2):
    return min(num1, num2)

def minSeq(s):    
    minVal = s[0]
    for val in s:
        minVal = min2(minVal, val)
    return minVal

class TestMinSeq(unittest.TestCase):
    def test_min_seq(self):
        data = [-1, 0, 2, 4]        
        result = minSeq(data)        
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()