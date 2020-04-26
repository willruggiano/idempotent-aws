import codecs
import re

from pathlib import Path
from setuptools import setup, find_packages

here = Path(__file__).parent


def read(*parts):
    return codecs.open(here.joinpath(*parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='boto-idempotent',
    version=find_version('src', 'boto_idempotent', '__init__.py'),

    description='Idempotency library for AWS resources',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    packages=find_packages(where='src', exclude=('test',)),
    package_dir={'': 'src'},

    python_requires='>=3.8',
    install_requires=[
        'botocore'
    ]
)
