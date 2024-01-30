from bitcoinlib.wallets import Wallet
from bitcoinlib.transactions import Transaction

class BitcoinWallet:
    def __init__(self, wallet_name="my_wallet"):
        try:
            # Try to load an existing wallet
            self.wallet = Wallet(wallet_name)
        except Exception as e:
            # If the wallet doesn't exist, create a new one
            if "Wallet not found" in str(e):
                self.wallet = Wallet.create(wallet_name)
            else:
                raise e

        self.address = self.wallet.get_key().address

    def generate_address(self, address_type='P2PKH'):
        if address_type not in ['P2PK', 'P2PKH', 'P2SH', 'P2WPKH', 'P2WSH', 'P2TR']:
            raise ValueError("Invalid address type")

        # Get the list of keys and select the last one
        keys = self.wallet.get_keys()
        if keys:
            new_key = keys[-1]
        else:
            new_key = self.wallet.get_key()
        
        # Derive subkey with specified type
        new_key = new_key.subkey(address_type)
        self.address = new_key.address
        return self.address
    
    def check_balance(self):
        return self.wallet.balance()

    def send_funds(self, to_address, amount):
        tx = Transaction.create(wallet=self.wallet)
        tx.add_output(to_address, amount)
        tx.sign()
        tx.send()

    def receive_funds(self):
        # Simulate receiving funds
        pass

    def transaction_history(self):
        return [tx.to_dict() for tx in self.wallet.transactions()]

# Example usage
if __name__ == "__main__":
    my_wallet = BitcoinWallet()

    print("Current Address:", my_wallet.address)
    print("Current Balance:", my_wallet.check_balance())

    # Generate different address types
    new_p2pk_address = my_wallet.generate_address('P2PK')
    new_p2pkh_address = my_wallet.generate_address('P2PKH')
    new_p2sh_address = my_wallet.generate_address('P2SH')
    new_p2wpkh_address = my_wallet.generate_address('P2WPKH')
    new_p2wsh_address = my_wallet.generate_address('P2WSH')
    new_p2tr_address = my_wallet.generate_address('P2TR')

    print("New P2PK Address:", new_p2pk_address)
    print("New P2PKH Address:", new_p2pkh_address)
    print("New P2SH Address:", new_p2sh_address)
    print("New P2WPKH Address:", new_p2wpkh_address)
    print("New P2WSH Address:", new_p2wsh_address)
    print("New P2TR Address:", new_p2tr_address)

    # Simulate receiving funds
    my_wallet.receive_funds()

    print("Updated Balance:", my_wallet.check_balance())

    # Send funds to another address
    to_address = "some_other_bitcoin_address"
    amount_to_send = 0.1
    my_wallet.send_funds(to_address, amount_to_send)

    print("Updated Balance after sending funds:", my_wallet.check_balance())

    # Display transaction history
    history = my_wallet.transaction_history()
    print("Transaction History:")
    for tx in history:
        print(tx)
