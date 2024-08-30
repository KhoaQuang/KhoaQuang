from setuptools import setup

setup(
    name='TK_calculator',
    version='0.0.1',
    packages=['TK_calculator'],
    install_requires=[
        'requests',
        'importlib; python_version == "3.11.9"',
        'tkinter',
    ],
)