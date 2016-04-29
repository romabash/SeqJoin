try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'SeqJoin joins two sequencing files taken from forward and reverse primers together',
    'author': 'Roma',
    'author_email': '',
    'version': '1.0',
    'install_requires': ['nose'],
    'packages': ['SeqJoin'],
    'scripts': [],
    'name': 'SeqJoin'
}

setup(**config)
