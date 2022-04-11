from bip44.utils import get_eth_addr
from bip32 import BIP32
import csv

# seed = "your seed here"
# xpriv = "your x priv here"
xpub = "your xpub with derivated path m/44'/60'/0'/0 here"
# change as necessary
NUMBER_OF_GENERATED_ADDRESSES = 5000

# w = BIP32.from_seed(seed)
# w = BIP32.from_xpriv(xpriv)
w = BIP32.from_xpub(xpub)
f = open('addresses.csv', 'w')
writer = csv.writer(f)

for i in range(NUMBER_OF_GENERATED_ADDRESSES):
    path = "m/{0}".format(i)
    pk = w.get_pubkey_from_path(path)
    row = get_eth_addr(pk)
    writer.writerow([i + 1, row])

f.close()
