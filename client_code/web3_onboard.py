# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Empiria Ltd
#
# This software is published at https://github.com/empiria/anvil-dapps

import anvil.js

Onboard = anvil.js.import_from("@web3-onboard/core").default
InjectedWallets = anvil.js.import_from("@web3-onboard/injected-wallets").default
Metamask = anvil.js.import_from("@web3-onboard/metamask").default
