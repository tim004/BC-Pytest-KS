from setuptools import setup, find_packages

setup(
    name='pytest-KS',
    extras_require=dict(tests=['pytest']),
    packages=find_packages(where='src'),
    packages_dir={"": "src"},
)
