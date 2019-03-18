import unittest
from list_sort import sort_list


class listsortTest(unittest.TestCase):

    def test_integers(self):
        self.assertEqual(sort_list(5), 'Invalid Input')
    def test_emptyList(self):
        self.assertEqual(sort_list([]) ,'This list is empty')
    def test_sortedList(self):
        self.assertNotEqual(sort_list([3,2,1,'y','r']), {'evens':[]})
        self.assertEqual(sort_list([3,2,1,'y','r']),{'evens': [2], 'odds': [1, 3], 'chars': ['r', 'y']})

if __name__ == '__main__':
    unittest.main()