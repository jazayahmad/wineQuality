from setuptools import setup, find_packages

setup(
    name="src",
    version="0.0.1",
    description="It's a Wine Quality package",
    author="Jazay A.",
    packages= find_packages(),
    license= "MIT"
)
# For creating distribution of the project:
''' python setup.py sdist '''

# For creating build of the project:
''' python setup.py bdist_wheel '''