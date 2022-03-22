from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='graph_lib',
    version='0.0.1',
    description='Graph library for python',
    long_description=readme,
    author='Saul Neri',
    author_email='contact@saulneri.com',
    url='https://github.com/saulno/graph_lib',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)