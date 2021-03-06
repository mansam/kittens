from setuptools import setup

setup(
    name='kittens',
    version='0.1.2',
    author='Samuel "mansam" Lucidi',
    author_email="mansam@csh.rit.edu",
    packages=['kittens'],
    url='http://pypi.python.org/pypi/kittens/',
    license='LICENSE',
    install_requires=['requests'],
    description='A means of sending friendly images of kittens to a target.',
    long_description=open('README.md').read()
)


