
import os
from setuptools import setup
from setuptools import find_packages

with open(os.path.join(os.path.dirname(__file__),'version')) as versionfile:
    version = versionfile.read().strip()

setup(name='Tiger',
    version=version,
    description='Terrific taskmaster',
    url='http://github.com/shellzoo/tiger',
    author='The Hathersage Group, Inc.',
    author_email='tiger@hathersage.group',
    license='MIT',
    packages=find_packages(),
    entry_points={'console_scripts':[
        'get=tiger.get:run',
        'list=tiger.list:run',
        ]},
    # package_data={'lemur':['lemur.ini']},
    zip_safe=False)
