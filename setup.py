from setuptools import setup

setup(name='decoy',
      version='0.1',
      description='Make decoy data for CI',
      url='http://github.com/alexandercbooth/decoy',
      author='Alexander Booth',
      author_email='alexander.c.booth@gmail.com',
      license='Apache',
      tests_require=['pytest'],
      test_suite='pytest', 
      packages=['decoy'],
      zip_safe=False)
