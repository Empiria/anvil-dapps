# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Empiria Ltd
#
# This software is published at https://github.com/empiria/anvil-dapps

from ._anvil_designer import TimeConditionTemplate
from .. import utils
from uuid import uuid4
import datetime as dt

_default = {
    "uid": None,
    "condition_type": "time_condition",
    "options": {
        "chain": None,
        "returnValueTest": {"comparator": ">=", "value": dt.datetime.now().timestamp()},
    },
}


class TimeCondition(TimeConditionTemplate):
    def __init__(self, item=None, **properties):
        self.comparator_dropdown.items = utils.comparators
        self.item = _default if item is None else item
        self.mode = "create" if item is None else "update"
        self.init_components(**properties)

    @property
    def timestamp(self):
        return dt.datetime.fromtimestamp(
            self.item["options"]["returnValueTest"]["value"]
        )

    @timestamp.setter
    def timestamp(self, value):
        self.item["options"]["returnValueTest"]["value"] = dt.datetime.timestamp(value)

    def save_button_click(self, **event_args):
        if self.mode == "create":
            self.item["uid"] = uuid4().hex
            self.item["options"]["chain"] = 0x13882
        self.raise_event("x-close-alert", value=self.item)

    def remove_button_click(self, **event_args):
        self.raise_event("x-close-alert", value="remove")
