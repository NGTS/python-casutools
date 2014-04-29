from setuptools import setup, find_packages
from glob import glob
import re

package_name = 'casutools'
version_str = re.search(r'^__version__\s+=\s+[\'"](.+)[\'"]',
        open('%s/version.py' % (package_name, )).read(),
        re.M).group(1)

setup(name=package_name,
        version=version_str,
        description='NGTS casutools python wrapper',
        author='Simon Walker',
        author_email='s.r.walker101@googlemail.com',
        maintainer='Simon Walker',
        maintainer_email='s.r.walker101@googlemail.com',
        url='http://github.com/NGTS/python-casutools',
        packages=find_packages(),
        long_description=open('README.md').read(),
        )
