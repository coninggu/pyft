# -*- coding: utf-8 -*-
import codecs
from setuptools import setup

install_requires = [
    'yapf==0.20.0',
    'gunicorn==19.7.1',
    'flask==0.12.2',
    'click',
    'setproctitle',
    'pytest',
    'pytest-cov',
]

with codecs.open('README.md', 'r', 'utf-8') as fd:
    setup(
        name='pyft',
        version=open('VERSION').read().strip(),
        description='Python Online Formatter',
        long_description=fd.read(),
        url='https://github.com/coninggu/pyft',
        author='coninggu',
        author_email='coninggu@gmail.com',
        license='',
        packages=['pyft'],
        install_requires=install_requires,
        python_requires='>=3.5',
        entry_points={
            'console_scripts': ['pyft=pyft.cli:main'],
        },
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.5',
        ],
    )
