from setuptools import find_packages, setup

setup(
    name='report_writer',
    packages=find_packages(),
    version='0.1.1',
    description='Lib for writing reports using docxtpl',
    author='Renato Martins',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
