from setuptools import setup, find_packages

version = '0.1'

setup(
    name='ckanext-rf',
    version=version,
    description="RF Interface for CKAN",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='C. List',
    author_email='cglist@cglist.net',
    url='http://github.com/rockfound/ckanext-rf',
    license='AGPL3.0',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.rf'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        rf=ckanext.rf.plugin:RFPlugin
    ''',
)
