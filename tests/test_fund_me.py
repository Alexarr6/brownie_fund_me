from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fund_me
from brownie import network, accounts, exceptions
import pytest


def test_can_fund_and_withdraw():

    # Cuando testeamos algo lo separamos en 3 categorias:

    # 1- Arrange(configurar todo lo  que tenemos que configurar)
    account = get_account()
    fund_me = deploy_fund_me()
    # 2- Act
    entrance_fee = fund_me.getEntranceFee()
    # print(entrance_fee)
    print(fund_me.addressToAmountFunded)
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    # 3- Assert
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee

    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0

    # Para testearlo usamos: brownie test


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    # Con esto le indicamos que si nos sale un mensaje de error es que esta bien!
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})
