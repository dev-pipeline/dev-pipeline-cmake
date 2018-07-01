#!/usr/bin/python3

"""This modules supports building CMake projects."""

import devpipeline_plugins.cmake.cmake


def get_builders():
    return {
        "cmake": devpipeline_plugins.cmake.cmake._make_cmake
    }
