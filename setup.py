from setuptools import setup, find_packages

setup(
    name='st_format',
    version='0.1',
    description='Utility functions for enhancing Streamlit apps',
    author='Guillermo Cerato',
    author_email='gcerato@gmail.com',
    url='https://github.com/willy71/st_format',
    packages=find_packages(),
    install_requires=[
        'streamlit',
    ],
)