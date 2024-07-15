# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Empiria Ltd
#
# This software is published at https://github.com/empiria/anvil-dapps

import re


def error_msg(error, error_map, default=None):
    for pattern, value in error_map:
        if re.search(pattern, str(error)):
            return value
    return default
