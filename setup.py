try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = [
           'description': 'New Project',
           'author': 'Patricia Scott',
           'url': 'URL to find it,
           'download_url': 'Where to download it',
           'author_email': 'my email',
           'version': '0.1',
           'install_requires': ['pytest'],
           'packages': ['NAME'],
           'scripts': [],
           'name': 'projectname'
]

setup(**config)
