import os
from setuptools import setup, find_packages

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# Package dependencies
install_requires = [
    "wagtail>=2.8.1",
    "wagtailfontawesome>=1.1.4",
    "wagtail-color-panel>=1.2.0",
]

# Testing dependencies
testing_extras = [
]

# Documentation dependencies
documentation_extras = [
]

setup(
    name='wagtail_block_collection',
    version=__import__('wagtail_block_collection').__version__,
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='A Collection of wagtail steam fields',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/slice-of-bits/wagtail-block-collection',
    author='SliceOfBits',
    author_email='matthijs@sliceofbits.com',
    keywords=['WAGTAIL', 'STREAMFIELD', 'WAGTAIL_BLOCKS', 'WAGTAIL CMS'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Wagtail',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
    ],
    install_requires=install_requires,
    extras_require={
        'testing': testing_extras,
        'docs': documentation_extras
    },
)