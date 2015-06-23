"""
WebPages - python web framework
=====

This project designed for web developers who want to do more for the less time.
To create new project with Hello World and database connection you need few minutes.
No need to create own user registration and authentication system - save your time
and focus on your main task - create anaming product in short time.


Development version
-----

    https://github.com/webpages/webpages
    git clone git@github.com:webpages/webpages.git
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


version = '1.0.0a'


setup(
    name='WebPages',
    version=version,
    url='https://github.com/webpages/webpages',
    license='MIT',
    author='Anton Danilchenko',
    author_email='anton@danilchenko.me',
    description='WebPages - python web framework',
    keywords='web framework development',
    long_description=__doc__,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages=['webpages', 'webpages.middleware'],
    install_requires=['webob'],
    include_package_data=True,
    zip_safe=False,
    platforms='any'
)
