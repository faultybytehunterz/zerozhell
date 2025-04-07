#!/usr/bin/python3
import codecs
from setuptools import setup, find_packages

ZEROZHELL_VERSION = "4.0.4"
ZEROZHELL_DOWNLOAD = ('https://github.com/zerozhell/zerozhell/tarball/' + ZEROZHELL_VERSION)


def read_file(filename):
	"""
	Read a utf8 encoded text file and return its contents.
	"""
	with codecs.open(filename, 'r', 'utf8') as f:
		return f.read()



def read_requirements():
    """
    This Python function reads and returns the contents of a file named 'requirements.txt'.
    :return: The function `read_requirements()` reads the contents of the file 'requirements.txt' and
    returns a list of strings, where each string represents a line from the file.
    """
    with open('requirements.txt') as f: 
        return f.readlines() 


setup(
	name='zerozhell',
	packages=[
		'zerozhell',
		'zerozhell.configs',
		'zerozhell.mods',
		'zerozhell.core',
		'zerozhell.core.base',
		'zerozhell.core.utils'],
	package_data={
          'zerozhell.core': [
              'utils/*',
          ],
      },

	version=zerozhell_VERSION,
	description='ZeroZhell is a high level MITM framework',
	long_description=read_file('README.md'),
	long_description_content_type='text/markdown',
    # packages = find_packages(),
    entry_points ={ 
            'console_scripts': [ 
                'zerozhell = zerozhell.zerozhell:loop'
            ] 
        },

	license='MIT',
	author='Fardin Allahverdinazhand',
	author_email='0x0ptim0us@gmail.com',
	url='https://github.com/zerozhell/zerozhell',
	download_url=zerozhell_DOWNLOAD,
	keywords=['python3', 'zerozhell', 'wsf', 'MITM', 'wifi', 'arp spoof'],
	classifiers=[
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Natural Language :: English',
	],

	install_requires= read_requirements(),

)
