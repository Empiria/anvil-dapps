# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Empiria Ltd
#
# This software is published at https://github.com/empiria/anvil-dapps

from ._anvil_designer import SelectConditionTemplate


class SelectCondition(SelectConditionTemplate):
    def __init__(self, **properties):
        self.time_button.tag.target = "time_condition"
        self.rpc_button.tag.target = "rpc_condition"
        self.contract_button.tag.target = "contract_condition"
        self.init_components(**properties)

    def button_clicked(self, sender, **event_args):
        self.raise_event("x-close-alert", value=sender.tag.target)
