import unittest
import nesting_structure_comparison

class TestFunctions(unittest.TestCase):
    def test_longest_consec(self):
        #check true
        self.assertTrue(nesting_structure_comparison.same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] ))
        self.assertTrue(nesting_structure_comparison.same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ]))
        self.assertTrue(nesting_structure_comparison.same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ]))

        self.assertTrue(nesting_structure_comparison.same_structure_as([1,[[[1]]]],[2,[[[2]]]]))
        self.assertTrue(nesting_structure_comparison.same_structure_as([1,'[',']'],['[',']',1]))
        

        #check false
        self.assertFalse(nesting_structure_comparison.same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ]))
        self.assertFalse(nesting_structure_comparison.same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ]))
        self.assertFalse(nesting_structure_comparison.same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ]))

        self.assertFalse(nesting_structure_comparison.same_structure_as([],1))
        self.assertFalse(nesting_structure_comparison.same_structure_as([],{}))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)