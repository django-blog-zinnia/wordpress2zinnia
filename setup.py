"""Setup script of wodpress2zinnia"""
from setuptools import setup
from setuptools import find_packages

import zinnia_wordpress

setup(
    name='wordpress2zinnia',
    version=zinnia_wordpress.__version__,

    description='Import your WordPress blog into Zinnia',
    long_description=open('README.rst').read(),

    keywords='django, zinnia, wordpress',

    author=zinnia_wordpress.__author__,
    author_email=zinnia_wordpress.__email__,
    url=zinnia_wordpress.__url__,

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

    license=zinnia_wordpress.__license__,
    include_package_data=True,
    zip_safe=False
)
