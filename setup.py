from setuptools import setup

setup(name='chunkyjson',
      version='1.0',
      description='Python Json-Class Marshaling Library',
      url='http://github.com/otherview/chunkyjson',
      author='Pedro Gomes',
      author_email='pedro.gomes@qubit.pt',
      license='MIT',
      packages=['chunkyjson'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
      )