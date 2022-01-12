from brownie import AdvancedCollectible
from scripts.helpful_scripts import get_account, fund_with_link
from web3 import Web3


def main():
    account = get_account()
    advacned_collectible = AdvancedCollectible[-1]
    fund_with_link(advacned_collectible.address,
                   amount=Web3.toWei(0.1, "ether"))
    create_tx = advacned_collectible.createCollectible({"from": account})
    create_tx.wait(1)
    print("Collectible creatred!")
