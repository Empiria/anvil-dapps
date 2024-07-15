# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Empiria Ltd
#
# This software is published at https://github.com/empiria/anvil-dapps

import anvil.js
from ..utils import error_msg

_taco = anvil.js.import_from("@nucypher/taco")
_ethers = anvil.js.import_from("ethers").ethers

domains = _taco.domains
conditions = _taco.conditions

_error_map = [
    ("Ritual \d* is not finalized", "Ritual failed"),
    ("Decryption conditions not satisfied", "Decryption conditions not satisfied"),
]

_taco.initialize()


def encrypt(provider, domain, message, condition, ritual_id):
    web3_provider = _ethers.providers.Web3Provider(provider, "any")
    signer = web3_provider.getSigner()
    try:
        message_kit = _taco.encrypt(
            web3_provider, domain, message.encode(), condition, ritual_id, signer
        )
    except anvil.js.ExternalError as e:
        raise ValueError(error_msg(e, _error_map, "Encryption failed"))
    return message_kit.toBytes().hex()


def decrypt(provider, domain, ciphertext):
    uri = _taco.getPorterUri(domain)
    message_kit = _taco.ThresholdMessageKit.fromBytes(bytes.fromhex(ciphertext))
    web3_provider = _ethers.providers.Web3Provider(provider, "any")
    signer = web3_provider.getSigner()
    try:
        return _taco.decrypt(web3_provider, domain, message_kit, uri, signer).decode()
    except anvil.js.ExternalError as e:
        raise ValueError(error_msg(e, _error_map, str(e)))
