import unittest

# --- The Class to be Tested (SUT: System Under Test) ---
class Calculator:
    """A simple class with basic arithmetic operations."""
    
    def add(self, a, b):
        """Returns the sum of two numbers."""
        return a + b
    
    def subtract(self, a, b):
        """Returns the difference of two numbers."""
        return a - b

# --- The Test Class ---
class TestCalculator(unittest.TestCase):
    """Tests for the Calculator class."""

    def test_addition(self):
        """Test that addition works correctly."""
        calc = Calculator()
        # Assertion: Check if 1 + 2 equals 3
        self.assertEqual(calc.add(1, 2), 3, "Should be 3")
        # Another test case for addition
        self.assertEqual(calc.add(-5, 5), 0, "Should be 0")
        
    def test_subtraction(self):
        """Test that subtraction works correctly."""
        calc = Calculator()
        # Assertion: Check if 10 - 4 equals 6
        self.assertEqual(calc.subtract(10, 4), 6, "Should be 6")
        # Another test case for subtraction
        self.assertEqual(calc.subtract(0, 7), -7, "Should be -7")

    def test_addition_is_integer_result(self):
        """Test that the result of addition is an integer (for integer inputs)."""
        calc = Calculator()
        result = calc.add(5, 3)
        # Assertion: Check if the type of the result is an integer
        self.assertIsInstance(result, int, "Should be an integer")

# --- Running the Tests ---
if __name__ == '__main__':
    # This runs all methods starting with 'test_' in the TestCalculator class
    unittest.main()