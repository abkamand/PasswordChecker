import unittest
from check_pwd import check_pwd


class MyTestCase(unittest.TestCase):
    # checks if empty string returns false
    def test1(self):
        pw = ''
        self.assertFalse(check_pwd(pw), msg='Does not meet the requirements '
                                            '(num={})'.format(pw))

    # checks length, if a string of less than 8 chars returns false
    def test2(self):
        pw = 'Ab34567$'
        self.assertTrue(check_pwd(pw), msg='Does not meet the requirements '''
                                           '(num={})'.format(pw))


if __name__ == '__main__':
    unittest.main()
