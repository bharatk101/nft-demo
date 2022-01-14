from scripts.advanced.deploy_and_create import deploy_and_create
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account, get_contract
from brownie import network
import pytest



def test_can_create_advanced_collectible():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    advanced_collectible, creation_tx = deploy_and_create()
    requestId = creation_tx.events['requestedCollectibe']['requestId']
    random_number =777
    get_contract("vrf_coordinator").callBackWithRandomness(requestId, random_number, advanced_collectible.address, {"from":get_account()})
    assert advanced_collectible.tokenCounter() == 1
    assert advanced_collectible,tokenIdToBreed(0) == random_number % 3
    
