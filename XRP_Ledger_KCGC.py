# Define the network client
from xrpl.clients import JsonRpcClient
JSON_RPC_URL = "https://s.altnet.rippletest.net:51234/"
client = JsonRpcClient(JSON_RPC_URL)


# Create a wallet using the testnet faucet:
# https://xrpl.org/xrp-testnet-faucet.html
from xrpl.wallet import generate_faucet_wallet
KCGC_wallet = generate_faucet_wallet(client, debug=True)

# Create an account str from the wallet
KCGC_account = KCGC_wallet.classic_address

# Derive an x-address from the classic address:
# https://xrpaddress.info/
from xrpl.core import addresscodec
KCGC_xaddress = addresscodec.classic_address_to_xaddress(KCGC_account, tag=12345, is_test_network=True)
print("\nClassic address:\n\n", KCGC_account)
print("X-address:\n\n", KCGC_xaddress)


# Look up info about your account
from xrpl.models.requests.account_info import AccountInfo
acct_info = AccountInfo(
    account=KCGC_account,
    ledger_index="validated",
    strict=True,
)
response = client.request(acct_info)
result = response.result
print("response.status: ", response.status)
import json
print(json.dumps(response.result, indent=4, sort_keys=True))
