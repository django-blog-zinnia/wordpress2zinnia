"""Setup script of wodpress2zinnia"""
from setuptools import setup
from setuptools import find_packages

import wordpress2zinnia

setup(
    name='wordpress2zinnia',
    version=wordpress2zinnia.__version__,

    description='Import your WordPress blog into Zinnia',
    long_description=open('README.rst').read(),

    keywords='django, zinnia, wordpress',

    author=wordpress2zinnia.__author__,
    author_email=wordpress2zinnia.__email__,
    url=wordpress2zinnia.__url__,

    packages=find_packages(exclude=['demo_zinnia_wordpress']),
    classifiers=[
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'],

    license=wordpress2zinnia.__license__,
    include_package_data=True,
    zip_safe=False
)
