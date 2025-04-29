from util import *
import multiprocessing

def main():
    cs, secret_key_path, public_key_path = init_algo(0)
    generate_keys(cs, secret_key_path, public_key_path)
    size = 3
    tally = load_and_encrypt_tally(cs, size)


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    main()