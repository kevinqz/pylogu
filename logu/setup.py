from setuptools import setup, find_packages

setup(
    name='logu',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['httpx>=0.18.2'],
    python_requires='>=3.7',
    description='Logu - Python SDK',
    author='Kevin Saltarelli',
    author_email='kevinqz@gmail.com',
    url='https://github.com/kevinqz/logu-sdk',
)
