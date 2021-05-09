import unittest
from check_pwd import check_pwd


class MyTestCase(unittest.TestCase):
    # checks if empty string returns false
    def test1(self):
        pw = ''
        self.assertFalse(check_pwd(pw), msg='Does not meet the requirements '
                                            '(num={})'.format(pw))

    # checks length, if a string of 8 chars returns true
    def test2(self):
        pw = 'Ab34567$'
        self.assertTrue(check_pwd(pw), msg='Does not meet the requirements '''
                                           '(num={})'.format(pw))

    # checks length, if a string of greater than 20 chars returns false
    def test3(self):
        pw = 'Ab34567$8910111235670'
        self.assertFalse(check_pwd(pw), msg='Does not meet the requirements '
                                            '(num={})'.format(pw))

    # checks if pw that does not contain a lowercase letter returns false
    def test4(self):
        pw = 'AB345678$'
        self.assertFalse(check_pwd(pw), msg='Does not meet the requirements '
                                            '(num={})'.format(pw))

    # checks if pw that does not contain an uppercase letter returns false
    def test5(self):
        pw = 'ab345678$'
        self.assertFalse(check_pwd(pw), msg='Does not meet the requirements '
                                            '(num={})'.format(pw))

    # checks if pw that does not contain a digit returns false
    def test6(self):
        pw = 'aBcdefgh$'
        self.assertFalse(check_pwd(pw), msg='Does not meet the requirements '
                                            '(num={})'.format(pw))


if __name__ == '__main__':
    unittest.main()
