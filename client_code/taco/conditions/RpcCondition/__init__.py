# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Empiria Ltd
#
# This software is published at https://github.com/empiria/anvil-dapps

from ._anvil_designer import RpcConditionTemplate
from .. import utils
from uuid import uuid4

_default = {
    "uid": None,
    "condition_type": "rpc_condition",
    "options": {
        "chain": None,
        "method": "eth_getBalance",
        "parameters": [":userAddress", "latest"],
        "returnValueTest": {"comparator": ">=", "value": 0},
    },
}


class RpcCondition(RpcConditionTemplate):
    def __init__(self, item=None, **properties):
        self.comparator_dropdown.items = utils.comparators
        self.item = _default if item is None else item
        self.mode = "create" if item is None else "update"
        self.init_components(**properties)

    def save_button_click(self, **event_args):
        if self.mode == "create":
            self.item["uid"] = uuid4().hex
            self.item["options"]["chain"] = 0x13882
        self.raise_event("x-close-alert", value=self.item)

    def remove_button_click(self, **event_args):
        self.raise_event("x-close-alert", value="remove")
