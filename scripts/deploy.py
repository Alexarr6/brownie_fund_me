from brownie import FundMe, network, config, MockV3Aggregator

# Con __init__.py python sabe que puede importar desde otros scripts y paquetes en este proyecto
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)

from web3 import Web3


def deploy_fund_me():
    account = get_account()
    # Tenemos que pasar la direccion del precio de la comision al contrato fund_me
    # Podemos pasar las variables a los constructor a traves del deploy, poniendolo antes del from.

    # Que queremos?

    # Si estamos en una red persistente como rinkeby, usar la direccion asociada
    # De otra forma, deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        print(f"The active network is {network.show_active()}")
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()


# Vamos a añadir una nueva red a brownie para poder trabajar con otra ademas de con rinbeky:

# brownie networks add Ethereum ganache-local host=http://0.0.0.0:8545 chainid=1337

# Para pasarlo a Github tenemos que hacer:

# git init -b main (el nombre de la rama es main)

# Añadimos el nombre e email a la configuracion de git:

# git config user.name "Alexarr6"
# git config user.email "jandroariass@gmail.com"

# Para ver que archivos llevamos a git:

# git add .
# git status
