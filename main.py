from bitcoinlib.wallets import Wallet
from bitcoinlib.transactions import Transaction
from bitcoinlib.keys import HDKey

class BitcoinWallet:
    def __init__(self, wallet_name="my_wallet"):
        self.wallet = Wallet.create(wallet_name)
        self.address = self.wallet.get_key().address()
    
    def generate_address(self):
        new_key = self.wallet.get_key(index=len(self.wallet.keys))
        self.address = new_key.address()
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

    new_address = my_wallet.generate_address()
    print("New Address:", new_address)

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
