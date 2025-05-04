from lightphe import LightPHE
import json
import argparse
import pickle


# === Algorithm Configuration ===
def init_algo(algo, key=None):
    if algo == 0:
        phe = LightPHE(algorithm_name = "Paillier", keys=key)
    elif algo == 1:
        phe = LightPHE(algorithm_name = "Elliptic-Curve-ElGamal", keys=key)
    elif algo == 2:
        phe = LightPHE(algorithm_name = "Benaloh", keys=key)
    else:
        print("Invalid algorithm choice! :(")
    return phe

def algo_path(algo):
    if algo == 0:
        secret_key_path = "keys/paillier/secret.key"
        public_key_path = "keys/paillier/public.key"
    elif algo == 1:
        secret_key_path = "keys/elliptic_curve/secret.key"
        public_key_path = "keys/elliptic_curve/public.key"
    elif algo == 2:
        secret_key_path = "keys/benaloh/secret.key"
        public_key_path = "keys/benaloh/public.key"
    else:
        print("Invalid algorithm choice! :(")
    return secret_key_path, public_key_path
    
# === Key Management ===   
# Generate key and export it to key file  !!!Secret key saved in plaintext!!!
def generate_keys(phe, secret_key_path, public_key_path):
    phe.export_keys(secret_key_path)
    phe.export_keys(public_key_path, public = True)

# Load the keys from the files
def load_public_keys(public_key_path):
    with open(public_key_path, "r") as f:
        public_key_str = f.read()
        public_key = json.loads(public_key_str)
    return public_key
def load_private_keys(secret_key_path):
    with open(secret_key_path, "r") as f:
        private_key_str = f.read()
        private_key = json.loads(private_key_str)
    return private_key

# === Encryption ===
def load_and_encrypt_tally(cs, size):
    tally = [0] * size
    encrypted_tally = cs.encrypt(tally)
    return encrypted_tally

def save_encrypted_vote(encrypted_vote, file_path):
    with open(file_path, "wb") as f:
        pickle.dump(encrypted_vote, f)

def load_encrypted_vote(file_path):
    with open(file_path, "rb") as f:
        encrypted_vote = pickle.load(f)
    return encrypted_vote


def get_user_vote(size):
    print("\n=== Voting Ballot ===")
    for i in range(size):
        print(f"[{i}] Candidate {i}")
    
    while True:
        try:
            choice = int(input("\nEnter your choice (0-{}): ".format(size-1)))
            if 0 <= choice < size:
                # Create a vote array with 0s and a single 1 at the chosen position
                vote = [0] * size
                vote[choice] = 1
                return vote
            else:
                print(f"Invalid choice! Please enter a number between 0 and {size-1}")
        except ValueError:
            print("Please enter a valid number")



def parse_arg_server():
    parser = argparse.ArgumentParser(description="LightPHE Voting System Server")
    parser.add_argument("--algo", type=int, default=0, 
                        help="Algorithm choice: 0 for Paillier, 1 for Elliptic Curve ElGamal, 2 for Benaloh")
    parser.add_argument("--size", type=int, default=3,
                        help="Number of candidates")
    parser.add_argument("--generate", action="store_true",
                        help="Generate keys")
    return parser.parse_args()

def parse_arg_client():
    parser = argparse.ArgumentParser(description="LightPHE Voting System Client")
    parser.add_argument("-a", "--algo", type=int, default=0, 
                        help="Algorithm choice: 0 for Paillier, 1 for Elliptic Curve ElGamal, 2 for Benaloh")
    parser.add_argument("-s", "--size", type=int, default=3,
                        help="Number of candidates")
    return parser.parse_args()


