#!/usr/bin/python3

from setuptools import setup, find_packages

with open("README.rst") as f:
    long_description = f.read()

_VERSION = "0.5.0"

setup(
    name="dev-pipeline-cmake",
    version=_VERSION,
    package_dir={"": "lib"},
    packages=find_packages("lib"),
    install_requires=[
        "dev-pipeline-build >= {}".format(_VERSION),
        "dev-pipeline-core >= {}".format(_VERSION),
    ],
    entry_points={
        "devpipeline.builders": ["cmake = devpipeline_cmake.cmake:_CMAKE_TOOL"]
    },
    author="Stephen Newell",
    description="cmake plugin for dev-pipeline",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    license="BSD-2",
    url="https://github.com/dev-pipeline/dev-pipeline-cmake",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Utilities",
    ],
)
