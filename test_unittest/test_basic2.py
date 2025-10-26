from unittest import TestCase


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


class TestCalculator(TestCase):
    def test_add(self):
        result = add(10, 5)
        self.assertEqual(result, 15)

    def test_subtract(self):
        result = subtract(20, 5)
        self.assertEqual(result, 15)

    def test_multiply(self):
        result = multiply(3, 5)
        self.assertEqual(result, 15)

    def test_divide(self):
        result = divide(30, 2)
        self.assertEqual(result, 15)
