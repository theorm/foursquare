#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# (c) 2012 Mike Lewis

from setuptools import setup

#import foursquare
#version = str(foursquare.__version__)
# rl- stands for rate limiter, -x for version increment
version = 'rl20120716-4'

setup(
    name='foursquare',
    version=version,
    author='Mike Lewis',
    author_email='mike@fondu.com',
    url='http://github.com/mLewisLogic/foursquare',
    description='easy-as-pie foursquare wrapper library',
    long_description=open('./README.txt', 'r').read(),
    download_url='http://github.com/mLewisLogic/foursquare/tarball/master',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'License :: OSI Approved :: MIT License',
        ],
    packages=['foursquare'],
    package_data={'foursquare': ['*.pem']},
    install_requires=[
        'httplib2',
        'poster'
    ],
    license='MIT License',
    keywords='foursquare api',
    include_package_data=True,
    zip_safe=True,
)
