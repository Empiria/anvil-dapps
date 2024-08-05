# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Empiria Ltd
#
# This software is published at https://github.com/empiria/anvil-dapps

from ._anvil_designer import TacoConditionsTemplate
from .ConditionTemplate import ConditionTemplate
from .SelectCondition import SelectCondition
from . import utils
from ...taco import conditions
import anvil

try:
    from tabulator.Tabulator import Tabulator
except ImportError:
    raise ImportError(
        "The tabulator app is not available. You probably need to add it as a dependency."
    )

_no_conditions = """
Encryption will fail because no conditions have been defined.

Use the 'New' button to add a condition.
"""
_options = {
    "index": "uid",
    "pagination": False,
    "selectable": True,
    "header_visible": False,
    "use_model": True,
}
_columns = [
    {"field": "condition_type", "formatter": ConditionTemplate},
    {"field": "options", "visible": False},
]
_data = [
    {
        "uid": 1,
        "condition_type": "rpc_condition",
        "options": {
            "chain": 0x13882,
            "method": "eth_getBalance",
            "parameters": [":userAddress", "latest"],
            "returnValueTest": {"comparator": ">=", "value": 0},
        },
    }
]


class TacoConditions(TacoConditionsTemplate):
    def __init__(self, **properties):
        self.rich_text_1.content = _no_conditions
        self.tabulator = None
        self.init_components(**properties)

    def init_tabulator(self):
        self.tabulator = Tabulator(role="taco-conditions")
        self.tabulator.options = _options
        self.tabulator.columns = _columns
        self.tabulator.add_event_handler("row_click", self._on_row_click)
        self.content_panel.add_component(self.tabulator)

    @property
    def conditions(self):
        if not (self.tabulator and self.tabulator.initialized):
            return None
        return self.tabulator.getData()

    def _on_row_click(self, sender, row, **event_args):
        sender.deselectRow()
        row.select()
        condition = row.getData()
        attrs = utils.condition_types[condition["condition_type"]]
        response = anvil.alert(
            attrs["form"](item=condition), buttons=None, title=attrs["title"]
        )
        if response is None:
            return
        if response == "remove":
            row.delete()
            self.refresh_data_bindings()
            return
        row.update(response)
        row.reformat()
        self.refresh_data_bindings()

    @property
    def result(self):
        _conditions = [
            utils.condition_types[c["condition_type"]]["constructor"](c["options"])
            for c in self.tabulator.get_data()
        ]
        if not _conditions:
            return None
        if len(_conditions) == 1:
            return _conditions[0]
        cls = getattr(conditions.compound.CompoundCondition, "and")
        return cls(_conditions)

    def add_button_click(self, **event_args):
        if not self.tabulator:
            self.init_tabulator()
        target = anvil.alert(
            SelectCondition(), large=True, buttons=None, title="Select Condition Type"
        )
        response = (
            anvil.alert(
                utils.condition_types[target]["form"](),
                buttons=None,
                title=utils.condition_types[target]["title"],
            )
            if target
            else None
        )
        if response:
            self.tabulator.add_row(response)
            self.refresh_data_bindings()
