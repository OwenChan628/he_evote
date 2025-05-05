Partially Homomorphic Encryption Voting System implemented with LightPHE****

Requirements
pip: 
  pip install lightphe
  pip install flask

To generate key:
  python scripts/server.py --generate
  (use --algo to specify the algorithm's key)
  --algo 0: Paillier
  --algo 1: EllipticCurve-ElGamal
  --algo 2: Benaloh

Deploy on http:
  python scripts/app.py
It will run on 127.0.0.1:5000

You can visit 127.0.0.1:5000/results to see the decrypted results

