'''
1. Place the program check.py in same the folder as your programs.
2. To check your programs, run the check.py.
3. You can find your results in the file results.txt
'''

import sys
import unittest

class Test(unittest.TestCase):
    def test_p1(self):
        import exp1
        self.assertEqual(exp1.f(31),7)
        self.assertEqual(exp1.f(8),3)
        self.assertEqual(exp1.f(2),1)
        self.assertEqual(exp1.f(0),0)

    def test_p2(self):
        import exp2
        self.assertEqual(exp2.f(5,6,7),True)
        self.assertEqual(exp2.f(5,7,5),False)
        self.assertEqual(exp2.f(5,5,7),False)
        self.assertEqual(exp2.f(7,5,5),False)
        self.assertEqual(exp2.f(7,7,7),False)

    def test_p3(self):
        import exp3
        self.assertEqual(exp3.f("For Your Information"),"FYI")
        self.assertEqual(exp3.f("Hello Poland Krakow university"),"HPKu")

    def test_p4(self):
        import exp4
        self.assertEqual(exp4.f("5290312400019022"),"52**********9022")
        self.assertEqual(exp4.f("1111000022227777"),"11**********7777")

    def test_p5(self):
        import exp5
        self.assertEqual(exp5.f("101101"),True)
        self.assertEqual(exp5.f("1011201"),False)
        self.assertEqual(exp5.f("1010b1"),False)

    def test_p6(self):
        import exp6
        self.assertEqual(exp6.f(3124,True),6)
        self.assertEqual(exp6.f(20576,False),12)


if __name__ == '__main__':
    sys.stderr = open('results.txt', 'w', encoding="utf-8")
    unittest.main(verbosity=2)
