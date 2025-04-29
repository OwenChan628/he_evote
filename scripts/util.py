from lightphe import LightPHE

def init_algo(algo):
    if algo == 0:
        phe = LightPHE(algorithm_name = "Paillier")
        secret_key_path = "keys/paillier/secret.txt"
        public_key_path = "keys/paillier/public.txt"
    if algo == 1:
        phe = LightPHE(algorithm_name = "Exponential ElGamal")
        secret_key_path = "keys/exp_elga/secret.txt"
        public_key_path = "keys/exp_elga/public.txt"

    return phe, secret_key_path, public_key_path
    
# Generate key and export it to txt file  *Secret key saved in plaintext*
def generate_keys(phe, secret_key_path, public_key_path):
    phe.export_keys(secret_key_path)
    phe.export_keys(public_key_path, public = True)
    return phe

# Load the keys from the files
def load_public_keys(public_key_path):
    with open(public_key_path, "r") as f:
        public_key = f.read()
    return public_key
def load_private_keys(secret_key_path):
    with open(secret_key_path, "r") as f:
        private_key = f.read()
    return private_key

def load_and_encrypt_tally(cs, size)
    tally = [0] * size
    encrypted_tally = cs.encrypt(tally)
    return encrypted_tally


