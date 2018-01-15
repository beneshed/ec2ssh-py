from setuptools import setup, find_packages

setup(
    name='ec2ssh_py',
    version='0.1',
    packages=find_packages(),
    py_modules=['ec2ssh_cmd', 'ec2ssh_py'],
    install_requires=[
        'click',
        'click-completion',
        'jinja2'
    ],
    entry_points= {
        'console_scripts': ['ec2ssh_py=ec2ssh_cmd:cli']
    }
)