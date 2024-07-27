# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Empiria Ltd
#
# This software is published at https://github.com/empiria/anvil-dapps

# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Empiria Ltd
#
# This software is published at https://github.com/empiria/anvil_dapps
from ...taco import conditions
from .TimeCondition import TimeCondition
from .RpcCondition import RpcCondition
from .ContractCondition import ContractCondition
import datetime as dt

comparators = [
    ("Equal to", "="),
    ("Greather than", ">"),
    ("Greater than or equal to", ">="),
    ("Less than", "<"),
    ("Less than or equal to", "<="),
]

condition_types = {
    "time_condition": {
        "title": "Time Condition",
        "icon": "fa:clock-o",
        "constructor": conditions.base.time.TimeCondition,
        "form": TimeCondition,
    },
    "rpc_condition": {
        "title": "RPC Condition",
        "icon": "fa:link",
        "constructor": conditions.base.rpc.RpcCondition,
        "form": RpcCondition,
    },
    "contract_condition": {
        "title": "Contract Condition",
        "icon": "fa:handshake-o",
        "constructor": conditions.base.contract.ContractCondition,
        "form": ContractCondition,
    },
}


def description(condition):
    test = condition["options"]["returnValueTest"]
    condition_type = condition["condition_type"]
    if condition_type == "time_condition":
        return f"{test['comparator']} {dt.datetime.fromtimestamp(test['value']).isoformat()}"
    elif condition_type == "rpc_condition":
        return f"{condition['options']['method']} {test['comparator']} {test['value']}"
    elif condition_type == "contract_condition":
        return f"{condition['options']['standardContractType']} {condition['options']['method']} {test['comparator']} {test['value']}"
