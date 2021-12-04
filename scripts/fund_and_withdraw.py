from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]  # Cogemos el ultimo contrato
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entrance fee is {entrance_fee}")
    print("Funding...")
    fund_me.fund({"from": account, "value": entrance_fee})
    print("Funded!")


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print("Withdrawing...")
    fund_me.withdraw({"from": account})
    print("Withdraw!")


def main():
    fund()
    withdraw()
