# Drug Screening AutoML

This library is designed to optimize various models using AutoML for screening drug libraries. It provides functionalities for data preprocessing, model training, and library screening.

## Project Structure

The project has the following file structure:

```
drug-screening-automl
├── src
│   ├── __init__.py
│   ├── data_preprocessing
│   │   ├── __init__.py
│   │   └── known_inhibitors_preprocessor.py
│   ├── training
│   │   ├── __init__.py
│   │   └── model_trainer.py
│   ├── screening
│   │   ├── __init__.py
│   │   └── library_screener.py
│   └── utils
│       ├── __init__.py
│       └── helper_functions.py
├── tests
│   ├── __init__.py
│   ├── test_data_preprocessing.py
│   ├── test_training.py
│   └── test_screening.py
├── requirements.txt
├── setup.py
└── README.md
```

## Usage

To use this library, follow the steps below:

1. Install the required dependencies listed in `requirements.txt`.
2. Import the necessary classes and functions from the library modules.
3. Preprocess the known inhibitors data using the `KnownInhibitorsPreprocessor` class.
4. Train various models using the `ModelTrainer` class.
5. Screen drug libraries using the `LibraryScreener` class.

For detailed usage instructions and examples, refer to the documentation and the test cases in the respective modules.

## Testing

The library includes a comprehensive test suite located in the `tests` directory. Each module has its own test file containing test cases for the corresponding class or function. To run the tests, execute the test files using a test runner of your choice.

## License

This library is licensed under the MIT License. See the `LICENSE` file for more information.
```

Please note that you may need to update the content of the README.md file according to your specific project requirements and documentation style.