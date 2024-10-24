import unittest

def run_tests():
    # Load all test cases
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern='*.py')

    # Run the tests
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    run_tests()
