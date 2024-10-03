# File: /drug-screening-automl/drug-screening-automl/tests/__init__.py

# This file initializes the test suite.

# Import test modules
from . import test_data_preprocessing
from . import test_training
from . import test_screening

# Run the test suite
test_data_preprocessing.run_tests()
test_training.run_tests()
test_screening.run_tests()
