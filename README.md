# Partially Homomorphic Encryption Voting System implemented with LightPHE

## Requirements
```bash
pip install lightphe
pip install flask
```
To generate key:
```bash
python scripts/server.py --generate
```
&ensp;(use --algo to specify the algorithm's key)\
&ensp;--algo 0: Paillier\
&ensp;--algo 1: Exponential-ElGamal\
&ensp;--algo 2: Benaloh\
&ensp;--algo 3: Damgard-Jurik\
&ensp;--algo 4: Naccache-Stern\
&ensp;--algo 5: Okamoto-Uchiyama\

## Deploy on HTTP:
```bash
python scripts/app.py
```
It will run on 127.0.0.1:5000/

You can visit 127.0.0.1:5000/results to see the decrypted results

