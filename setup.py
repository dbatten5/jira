from setuptools import setup

setup(
    name='Jira',
    version='1.0',
    py_modules=['main'],
    install_requires=[
        'click',
        'gitpython',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        jira=main:cli
    '''
)
