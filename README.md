# Ethereum address generator from trezor

You can use this script and instructions to retrieve xpub from trezor and generate list of corresponding eth addresses.

Word of advise - !! never share your xpub with anyone !! unless you want to disclose to them your full history of all transactions.

I left commented sections of the code for initiation with seed (mnemonic) or master private key, but I strongly discourage you to use it.

## Usage

clone the repo and make sure you install following:

```
pip3 install --upgrade setuptools
pip3 install trezor
pip3 install "click<8.1"
```

connect your trezor and unlock it

```
trezorctl get-public-node -n "m/44'/60'/0'/0"
```

copy your xpub to the script

then install following:

https://github.com/darosior/python-bip32

```
pip3 install bip32
```

https://github.com/kigawas/python-bip44

```
pip3 install bip44
```

in the generate.py modify the number of generated addresses as needed and run

```
python3 generate.py
```
