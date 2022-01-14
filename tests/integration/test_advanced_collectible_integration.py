from brownie import network, AdvancedCollectible
import pytest
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_contract, get_account
from scripts.advanced.deploy_and_create import deploy_and_create
import time


def test_can_create_advacned_collectible_integration():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    # act
    advacned_collectible, creation_tx = deploy_and_create()
    time.sleep(60)
    # assert
    assert advacned_collectible.tokenCounter() == 1
