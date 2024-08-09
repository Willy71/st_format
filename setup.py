from setuptools import setup, find_packages

with open("readme.md", "r") as arq:
    readme = arq.read()

setup(
    name='st_format',
    version='0.2',
    license='MIT License',
    author='Guillermo Cerato',
    long_description=readme,
    long_description_content_type='text/markdown',
    author_email='gcerato@gmail.com',
    keywords='utilitys streamlit center text background',
    description='Utility functions for enhancing Streamlit apps',
    url='https://github.com/Willy71/st_format',
    packages=['st_format'],
    install_requires=['streamlit'],
)
