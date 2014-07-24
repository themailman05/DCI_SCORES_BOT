from distutils.core import setup

setup(
    name='DCI_SCORES_BOT',
    version='0.1.0',
    author='Liam Sargent',
    author_email='liam.t.sargent@gmail.com',
    packages=['DCI_SCORES_BOT', 'DCI_SCORES_BOT.test'],
    scripts=['bin/run.py'],
    url='http://pypi.python.org/pypi/TowelStuff/',
    license='LICENSE.txt',
    description='A reddit Bot for posting DCI Scores in realtime',
    long_description=open('README.txt').read(),
    install_requires=[
        "praw >= 2.1.17",
        "BeautifulSoup >= 3.2.1",
    ],
)