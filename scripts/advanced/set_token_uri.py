from brownie import network, AdvancedCollectible
from scripts.helpful_scripts import OPENSEA_URL, get_account, get_breed

dog_metadata_dic = {
    "PUG": "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmdryoExpgEQQQgJPoruwGJyZmz6SqV4FRTX1i73CT3iXn?filename=1-SHIBA_INU.json",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmbBnUjyHHN7Ytq9xDsYF9sucZdDJLRkWz7vnZfrjMXMxs?filename=2-ST_BERNARD.json",
}


def main():
    print(f"workinf on {network.show_active()}")
    advacned_collectible = AdvancedCollectible[-1]
    number_of_collectible = advacned_collectible.tokenCounter()
    print(f"you have {number_of_collectible} tokenId's")
    for token_id in range(number_of_collectible):
        breed = get_breed(advacned_collectible.tokenIdToBreed(token_id))
        if not advacned_collectible.tokenURI(token_id).startswith("https://"):
            print(f"Setting token URI of {token_id}")
            set_tokenURI(token_id, AdvancedCollectible,
                         dog_metadata_dic[breed])


def set_tokenURI(token_id, nft_contract, tokenURI):
    account = get_account()
    tx = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
    tx.wait(1)
    print(
        f"Awesome view nft at {OPENSEA_URL.format(nft_contract.address, token_id)}")
