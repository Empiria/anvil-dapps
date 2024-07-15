# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Empiria Ltd
#
# This software is published at https://github.com/empiria/anvil-dapps

from ._anvil_designer import ConditionTemplateTemplate
from .. import utils


class ConditionTemplate(ConditionTemplateTemplate):
    def __init__(self, item, **properties):
        attrs = utils.condition_types[item["condition_type"]]
        self.icon = attrs["icon"]
        self.title = attrs["title"]
        self.item = item
        self.init_components(**properties)

    @property
    def detail(self):
        return utils.description(self.item)
