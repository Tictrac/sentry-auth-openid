#!/usr/bin/env python
"""
sentry-auth-openid
==================

:copyright: (c) 2016 Functional Software, Inc
"""
from setuptools import setup, find_packages


install_requires = [
    'sentry>=7.0.0',
]

tests_require = [
    'flake8>=2.0,<2.1',
]

setup(
    name='sentry-auth-openid',
    version='1.0.0',
    author='lfbvr',
    author_email='',
    url='https://github.com/LFBVR/sentry-auth-openid',
    description='OpenID authentication provider for Sentry',
    long_description=__doc__,
    license='Apache 2.0',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={'tests': tests_require},
    include_package_data=True,
    entry_points={
        'sentry.apps': [
            'auth_openid = sentry_auth_openid',
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
