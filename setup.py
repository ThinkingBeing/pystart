"""setup file"""

from setuptools import setup

setup(
    setup_requires=['pbr', 'setuptools'],
    pbr=True,
    test_suite='main.tests',
    tests_require=['nose']
)
