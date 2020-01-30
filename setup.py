from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='whendidit',
      version='0.1',
      description='Remember when it happened',
      long_description=readme(),
      url='http://github.com/RyanSkraba/whendidit',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: Apache Software License'
      ],
      author='Ryan Skraba',
      author_email='ryan@skraba.com',
      license='ASL',
      packages=['whendidit'],
      install_requires=[
          'avro-python3'
      ],
      zip_safe=False)
