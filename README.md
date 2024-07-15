# Anvil Dapps
A dependency for building distributed applications (dapps) using the [Anvil](https://anvil.works) framework.

## Installation
Add the library as a third party dependency to your app with the token `RK36FKDUFUF2SV2C`.

## Docs
Anvil Dapps provides a wrapper for the following libraries:

* [Web3-Onboard](#web3-onboard) - A user-friendly interface for connecting to Ethereum wallets.
* [TACo](#taco) - Decentralised end-to-end encryption for secure data sharing.

### Web3-Onboard
To be read in conjunction with the [Web3-Onboard docs](https://onboard.blocknative.com/docs/overview/introduction).

#### Quick Start
To get started with Web3-Onboard, define the chains and wallets you want to support in your app and initialise the Onboard instance. e.g. To support the Polygon Amoy testnet chain with the MetaMask wallet and any wallets injected into the browser via extensions:

```python
from anvil_dapps import web3_onboard as w3o

amoy = {
    "id": 0x13882,
    "token": "MATIC",
    "label": "Polygon Amoy Testnet",
    "rpcUrl": "https://rpc-amoy.polygon.technology/",
}
wallets = [w3o.Metamask({"options": {"extensionOnly": False}}), w3o.InjectedWallets()]
onboard = w3o.Onboard(chains=[amoy], wallets=wallets)
wallet = onboard.connectWallet()[0]
```

### TACo
To be read in conjunction with the [TACo docs](https://docs.threshold.network/applications/threshold-access-control).

#### Quick Start
Assuming you have a connected wallet, you can use TACo to encrypt and decrypt data.

e.g. To encrypt a message with a condition stored on the Polygon Amoy testnet that the current date must be no earlier than 1st January 2024:

```python
from anvil_dapps import taco

domain = taco.domains.TESTNET
ritual_id = 0
message = "Hello, World!"
condition = taco.TimeCondition({"chain": 0x13882, "returnValueTest": {"comparator": ">", "value": 1704067200}})
ciphertext = taco.encrypt(wallet.provider, domain, message, [condition], ritual_id)
```

and to decrypt the message:

```python
plaintext = taco.decrypt(wallet.provider, domain, ciphertext)
```

#### Conditions
Anvil Dapps also includes a UI component for creating conditions which you should find in your app's component library.

You can use its `result` property to get the condition object to pass to the `encrypt` function.
