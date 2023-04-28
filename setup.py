try:
    from setuptools import setup, find_namespace_packages
except ImportError:
    from distutils.core import setup, find_namespace_packages
 

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setup(
    name='RuNerLib',
    version='0.0.1',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_namespace_packages(include=['RuNerLib','RuNerLib.*']),
    install_requires=REQUIREMENTS
)
