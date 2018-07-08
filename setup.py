#!/usr/bin/python3

from setuptools import setup, find_packages

setup(
    name="dev-pipeline-cmake",
    version="0.2.0",
    package_dir={
        "": "lib"
    },
    packages=find_packages("lib"),

    install_requires=[
        'dev-pipeline-core >= 0.2.0'
    ],

    entry_points={
        'devpipeline.builders': [
            'cmake = devpipeline_cmake:_CMAKE_TOOL',
        ]
    },

    author="Stephen Newell",
    description="cmake plugin for dev-pipeline",
    license="BSD-2",
    url="https://github.com/dev-pipeline/dev-pipeline-cmake",
)
