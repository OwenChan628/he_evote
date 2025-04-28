from util import *
import multiprocessing

def main():
    # Init
    cs, secret_key_path, public_key_path = init_algo(0)
    # Generate encryption keys
    generate_keys(cs, secret_key_path, public_key_path)

    # Encrypt the tally
    size = 3
    tally = [0] * size
    encrypted_tally = cs.encrypt(tally)



if __name__ == '__main__':
    # Optional on macOS to avoid recursive process spawning
    multiprocessing.set_start_method('spawn')
    main()