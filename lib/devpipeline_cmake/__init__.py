#!/usr/bin/python3

"""This modules supports building CMake projects."""

import devpipeline_cmake.cmake


def make_cmake(current_configuration, common_wrapper):
    return devpipeline_cmake.cmake._make_cmake(current_configuration,
                                               common_wrapper)

_CMAKE_TOOL = (make_cmake, "CMake build system generator.")
