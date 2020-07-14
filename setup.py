from setuptools import setup, find_packages
setup(
    name="bitport-cli",
    version="1.0",
    packages=find_packages(),
    scripts=["bitport"],
    install_requires=["requests"],
    author="Chris Ellsworth",
    author_email="chris@ellsworth.io",
    description="Bitport.io command-line interface",
    url="https://github.com/chrisellsworth/bitport-cli"
)
