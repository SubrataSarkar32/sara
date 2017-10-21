#!/usr/bin/env python

try:
    from setuptools import setup

    from pyhinengphonetic import __version__

    setup(name='sara',
          version='1.0',
          description='Virtual Assistant',
          long_description=open('README.md', 'rt').read(),
          author='Subrata Sarkar',
          author_email='subrotosarkar32@gmail.com',
          url='https://github.com/SubrataSarkar32/sara',
          packages=['sara'],
          package_data = {'pyhinengphonetic': ['*.md', '*.jpg']},
          include_package_data = True,
          install_requires=['PIL','psutil','speech_recognition'],
          license='GNU GPL v2 or later',
          zip_safe=True,
          classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2.7',
            ]
          )

except ImportError:
    print 'Install setuptools'