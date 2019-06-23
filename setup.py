#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='django-singleton',
    version='0.2.0',
    description='Reusable singleton models for Django (originally by Chris Davis)',
    author='Nemesis Fixx',
    author_email='joewillrich@gmail.com',
    url='https://github.com/NuChwezi/django-singleton',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
