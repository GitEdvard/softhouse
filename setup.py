from setuptools import setup, find_packages

setup(
    name="stock-winners",
    version='0.0.1',
    description="Show todays stock winners",
    long_description="Show todays stock winners from a REST API, returning data in json format",
    author="Edvard Englund",
    author_email='edvardenglund@yahoo.se',
    packages=find_packages(exclude=["tests*"]),
    entry_points={
        'console_scripts': [
            'stock-winners = stock_winners.cli:start'
        ]
    }
)

