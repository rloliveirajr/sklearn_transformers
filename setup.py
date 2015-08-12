from setuptools import setup, find_packages

setup(
    name='Trans4mers',
    version='0.0.1',
    author='Roberto Oliveira Jr',
    author_email='rloliveirajr@gmail.com',
    description='Implements several methods based on sklearn.transformers.',
    url='https://github.com/rloliveirajr/sklearn_tranformers',
    packages=find_packages(exclude=['tests']),
    scripts=[],
    install_requires=['numpy', 'scikit-learn'],
    tests_require=['pytest', 'freezegun'],
)
