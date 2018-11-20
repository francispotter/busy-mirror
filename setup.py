
import os
from setuptools import setup
from setuptools import find_packages

with open(os.path.join(os.path.dirname(__file__),'version')) as versionfile:
    version = versionfile.read().strip()

commands_dir = os.path.join(os.path.dirname(__file__),'todo','commands')
command_files = [f for f in os.listdir(commands_dir) if f[0] != '_']
commands = [f.split('.')[0] for f in command_files]
scripts = [f"{n}=todo.commands.{n}:run" for n in commands]

setup(name='Todo',
    version=version,
    description='Command-line task and plan management tool',
    url='http://gitlab.com/francispotter/todo',
    author='Francis Potter',
    author_email='todo@fpotter.com',
    license='MIT',
    packages=find_packages(),
    entry_points={'console_scripts':scripts},
    # data_files=[('/usr/share/shellzoo/zshrc/',['todo.sh'])],
    # package_data={'lemur':['lemur.ini']},
    zip_safe=False)
