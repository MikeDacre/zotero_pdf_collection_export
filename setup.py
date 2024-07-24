#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='zotero_pdf_exporter',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pyzotero',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'zotero_pdf_exporter=main:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A command line tool to export PDFs from Zotero organized by collections',
    url='https://github.com/yourusername/zotero_pdf_exporter',
)
