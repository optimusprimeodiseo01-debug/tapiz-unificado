from web3 import Web3
import json
import os

INFURA_URL = os.getenv("INFURA_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
ACCOUNT = Web3.to_checksum_address(os.getenv("ACCOUNT"))

w3 = Web3(Web3.HTTPProvider(INFURA_URL))

def deploy():
    assert w3.is_connected(), "No conecta a Infura"

    # --- ABI + BYTECODE (compilado previamente) ---
    with open("contracts/Tapiz.json") as f:
        contract_json = json.load(f)

    abi = contract_json["abi"]
    bytecode = contract_json["bytecode"]

    contract = w3.eth.contract(abi=abi, bytecode=bytecode)

    # Primos iniciales (tapiz base)
    primes = [2, 3, 5]

    nonce = w3.eth.get_transaction_count(ACCOUNT)

    tx = contract.constructor(primes).build_transaction({
        "chainId": 11155111,  # Sepolia
        "gas": 2000000,
        "gasPrice": w3.to_wei("20", "gwei"),
        "nonce": nonce,
    })

    signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

    print("TX:", tx_hash.hex())

    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Contrato desplegado en:", receipt.contractAddress)

if __name__ == "__main__":
    deploy()
