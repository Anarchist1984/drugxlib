import unittest
from drug_screening_automl.src.data_preprocessing.known_inhibitors_preprocessor import KnownInhibitorsPreprocessor

class TestDataPreprocessing(unittest.TestCase):
    def setUp(self):
        # Set up any necessary test data or objects
        pass

    def tearDown(self):
        # Clean up any resources used by the test
        pass

    def test_preprocessing(self):
        # Test the preprocessing functionality of KnownInhibitorsPreprocessor
        preprocessor = KnownInhibitorsPreprocessor()
        # Add your test cases here

if __name__ == '__main__':
    unittest.main()