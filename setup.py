from setuptools import setup, find_packages

REQUIRES = [
    'pandas==0.24.1',
]
TESTS_REQUIRES = [
    'zope.testrunner==4.9.2',
]


setup(
    name='pandas_diff',
    version='0.0.1',
    author='Simon Brand',
    tests_require=TESTS_REQUIRES,
    entry_points={
        'console_scripts': [
            'zope-testrunner = zope.testrunner:run',
            'diff_dataframes = pandas_diff.dataframe:main',
        ],
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=REQUIRES)
