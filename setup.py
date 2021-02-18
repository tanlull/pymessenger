from setuptools import setup

installation_requirements = [
    'requests',
    'requests-toolbelt',
    'six'
]

try:
    import enum
    del enum
except ImportError:
    installation_requirements.append('enum')

setup(
    name='pymessenger4',
    packages=['pymessenger4'],
    version='1.0.0',
    install_requires=installation_requirements,
    description="Python Wrapper for Facebook Messenger Platform",
    author='Tanya S.',
    author_email='tanlull@gmail.com',
    url='https://github.com/tanlull/pymessenger4',
    download_url='https://github.com/tablull/pymessenger4/tarball/1.0.0',
    keywords=['facebook messenger', 'python', 'wrapper', 'bot', 'messenger bot'],
    classifiers=[],
)
