from configparser import ConfigParser
from io import open
from pathlib import Path

from setuptools import setup

from zappa import __version__

with open("README.md", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

pipfile = ConfigParser()
pipfile.read(Path(__file__).parent.resolve() / "Pipfile")

required = []
for name, version in pipfile["packages"].items():
    if version == '"*"':
        required.append(name)
    elif "==" in version:
        required.append("{}{}".format(name, version.strip('"')))
    elif name == "zappa":
        required.append("zappa@git+https://github.com/Mealing-dev/zappa@master")
    else:
        required.append("{}{}".format(name, version.strip('"')))

test_required = [
    "{}{}".format(name, version.strip('"')) if version != '"*"' else name
    for name, version in pipfile["dev-packages"].items()
]

setup(
    name="zappa-warm",
    version=__version__,
    packages=["zappa"],
    install_requires=required,
    tests_require=test_required,
    test_suite="nose.collector",
    include_package_data=True,
    license="MIT License",
    description="Server-less Python Web Services for AWS Lambda and API Gateway",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mealing-dev/Zappa",
    author="Knewnew Developers",
    author_email="dev.knewnew@gmail.com",
    entry_points={
        "console_scripts": [
            "zappa=zappa.cli:handle",
            "z=zappa.cli:handle",
        ]
    },
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 3.0",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
