from setuptools import setup
import unittest
with open('README.rst', 'r') as f:
    readme = f.read()
def testsuite():
	test_loader = unittest.TestLoader()
	test_suite = test_loader.discover('tests', pattern='test*.py')
	return test_suite
setup(name='ojet',
      version='0.11.0',
      long_description=readme,
      description='Create wrapper around Oracle Jet to hide as much as possible HTML and Javascript',
      author='Gerard Duval',
      author_email='gerard.duval@gdsoftconsulting.com',
      url='https://github.com/gduvalsc/ojet',
      license='GPL',
      packages=['ojet'],
      classifiers=[ "Development Status :: 3 - Alpha", "Topic :: Utilities", "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)"],
      test_suite="setup.testsuite",
      zip_safe=False)
