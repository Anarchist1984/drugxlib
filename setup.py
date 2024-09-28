from setuptools import setup, find_packages

setup(
    name='drug-screening-automl',
    version='1.0.0',
    author='Your Name',
    author_email='your@email.com',
    description='A Python library for drug library screening using AutoML',
    packages=find_packages(),
    install_requires=[
        'autogluon-tabular',  # Add any additional dependencies here
    ],
)