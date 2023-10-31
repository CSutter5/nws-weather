from setuptools import setup, find_packages

setup(
    name='NWS_Weather',
    version='1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'geopy'
    ],
    author='Colin Sutter',
    author_email='contact@csutter.dev',
    description='A package for retrieving weather data from the National Weather Service',
    url='https://github.com/Pizzarules668/NWS_Weather',
)
