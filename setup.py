#!/usr/bin/python
#coding: utf-8

from setuptools import setup, find_packages

version = "1.0"
author = "Proversity.org Ltd"

setup(
    name='bibblio',
    version=version,
    author=author,
    author_email='antonio@proversity.org',
    url='http://docs.bibblio.apiary.io/',
    description='Python wrapper of Bibblio API',
    long_description='Python wrapper of Bibblio API',
    download_url='https://github.com/proversity-org/bibblio-api-python/archive/master.zip',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        ],
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    license='MIT License',
    keywords='Proversity.org Bibblio API Python wrapper',
    include_package_data=True,
    zip_safe=True,
)
