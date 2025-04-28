from util import *
import multiprocessing

secret_key_path = "keys/paillier_secret.txt"
public_key_path = "keys/paillier_public.txt"

def main():
    # Generate encryption keys
    cs = generate_keys(secret_key_path, public_key_path)

    # Encrypt the tally
    size = 3
    tally = [0] * size
    encrypted_tally = cs.encrypt(tally)
    #print(encrypted_tally)

    vote = [0,1,0]
    encrypted_vote = cs.encrypt(vote)
    #print(encrypted_vote)

    sum = encrypted_tally + encrypted_vote
    print(cs.decrypt(sum))


if __name__ == '__main__':
    # Optional on macOS to avoid recursive process spawning
    multiprocessing.set_start_method('spawn')
    main()