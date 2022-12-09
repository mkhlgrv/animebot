from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='animebot',
    version='0.1',
    description='Animebot',
    long_description=long_description,
    author='arsnvslv, mkhlgrv',
    packages=['src']  #same as name
    # install_requires=['wheel', 'bar', 'greek'], #external packages as dependencies
)
