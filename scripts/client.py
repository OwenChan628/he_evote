from util import *
import multiprocessing

def main():
    #Just for testing
    public_key_path = "keys/paillier/public.key"

    public_key = load_public_keys(public_key_path)
    cs = LightPHE(algorithm_name="Paillier", keys=public_key)
    vote = [0, 0, 1]
    encrypted_vote = cs.encrypt(vote)
    print("Encrypted vote:", encrypted_vote)

if __name__ == '__main__':
    # Set multiprocessing start method to 'spawn' on macOS
    multiprocessing.set_start_method('spawn')
    main()