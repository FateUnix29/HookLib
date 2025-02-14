# Setup script for hooklib.
# See hooklib.py for more information.

from setuptools import setup

setup(name='hooklib',
    version='0.0.1',
    description='HookLib - Modify code of functions at runtime for modularity and "mods".',
    author='FateUnix29',
    maintainer='FateUnix29',
    url='https://github.com/FateUnix29/HookLib',
    download_url='https://github.com/FateUnix29/HookLib/releases/latest',
    packages=['hooklib'],
    scripts=['./hooklib.py'],
    license='GPLv3',
    long_description='HookLib - Modify code of functions at runtime for modularity and "mods".',
    long_description_content_type='text/markdown',
    requires=['asyncio'])