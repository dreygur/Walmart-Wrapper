import setuptools

requirements = [
  'lxml',
  'requests',
]

test_requirements = [
  'pytest',
  'requests-mock',
]

setuptools.setup(
  name="py-walmart",
  version="0.0.1",
  url="https://github.com/rafsanbillah",

  author="Rafsan Billah",
  author_email="rafsanbillah@gmail.com",

  description="Walmart Marketplace API",
  long_description=open('README.rst').read(),

  packages=setuptools.find_packages(),

  install_requires=requirements,

  classifiers=[
    'Development Status :: 2 - Pre-Alpha',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9'
  ],
  test_suite='tests',
  tests_require=test_requirements
)
