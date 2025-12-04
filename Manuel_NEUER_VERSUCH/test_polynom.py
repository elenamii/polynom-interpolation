from polynom import Polynom
import unittest

class TestPolynom(unittest.TestCase):
    def test_multiplication(self):
        # (x + 1) * (x - 1) = x^2 - 1
        p1 = Polynom([1, 1]) # 1 + x
        p2 = Polynom([-1, 1]) # -1 + x
        p3 = p1 * p2
        # Expected: -1 + 0x + 1x^2 -> [-1, 0, 1]
        self.assertEqual(p3.coeffs, [-1, 0, 1])
        print(f"({p1}) * ({p2}) = {p3}")

        # (x + 2) * (x + 3) = x^2 + 5x + 6
        p4 = Polynom([2, 1])
        p5 = Polynom([3, 1])
        p6 = p4 * p5
        # Expected: 6 + 5x + 1x^2 -> [6, 5, 1]
        self.assertEqual(p6.coeffs, [6, 5, 1])
        print(f"({p4}) * ({p5}) = {p6}")

    def test_evaluation(self):
        # P(x) = x^2 - 1
        p = Polynom([-1, 0, 1])
        
        # P(2) = 4 - 1 = 3
        val = p.horner(2)
        self.assertEqual(val, 3)
        print(f"P(x)={p}, P(2)={val}")

        # P(0) = -1
        val = p.horner(0)
        self.assertEqual(val, -1)
        print(f"P(x)={p}, P(0)={val}")

if __name__ == '__main__':
    unittest.main()
