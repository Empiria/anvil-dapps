# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Empiria Ltd
#
# This software is published at https://github.com/empiria/anvil-dapps
"""Generate an import map and inject it into anvil.yaml

To run this, you will need to install the jspm CLI tool: https://jspm.org/getting-started

The resulting import map will be injected into anvil.yaml under the key `native_deps.import_map`.

That's editable from within the IDE, but you have to navigate to it manually. Go to
native libraries in the usual way but then, in the URL, replace 'native-libraries' with
'native-deps'.
"""

import subprocess
import io
import yaml

JSPMIO_MODULES = (
    "@nucypher/taco",
    "@web3-onboard/core",
    "@web3-onboard/injected-wallets",
    "@web3-onboard/metamask",
    "ethers",
)
RESOLUTIONS = {"ethers": "npm:ethers@5.7.2"}
ENVIRONMENTS = "production", "browser", "module"


def str_presenter(dumper, data):
    presenter = dumper.represent_scalar("tag:yaml.org,2002:str", data)
    if len(data.splitlines()) > 1:
        presenter.style = "|"
    return presenter


yaml.add_representer(str, str_presenter)
yaml.representer.SafeRepresenter.add_representer(str, str_presenter)


def generate_importmap(modules, environments, resolutions):
    environments = ",".join(environments)
    modules = " ".join(modules)
    resolutions = " ".join([f"-r {key}={value}" for key, value in resolutions.items()])

    cmd = f"jspm link -e {environments} {resolutions} --stdout {modules}"
    result = subprocess.run(cmd, shell=True, capture_output=True)
    buffer = io.BytesIO()
    buffer.write(result.stdout)
    buffer.seek(0)
    return buffer.read().decode()


def main():
    importmap = generate_importmap(JSPMIO_MODULES, ENVIRONMENTS, RESOLUTIONS)
    with open("anvil.yaml") as f:
        anvil_yaml = yaml.safe_load(f)
    anvil_yaml["native_deps"]["import_map"] = importmap
    with open("anvil.yaml", "w") as f:
        yaml.dump(anvil_yaml, f)


main()
