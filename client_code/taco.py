# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Empiria Ltd
#
# This software is published at https://github.com/empiria/anvil-dapps
import anvil.js

_taco = anvil.js.import_from("@nucypher/taco")

conditions = _taco.conditions
decrypt = _taco.decrypt
domains = _taco.domains
encrypt = _taco.encrypt
get_porter_uri = _taco.getPorterUri
initialize = _taco.initialize
