from util import *
import multiprocessing

def main():
    args = parse_arg_server()
    algo = args.algo
    size = args.size
    gen_key = args.generate
    print(f"Algorithm choice: {algo}, Number of candidates: {size}, Key generation: {gen_key}")

    if gen_key:
        print("Generating keys...")
        cs = init_algo(algo)
        secret_key_path, public_key_path = algo_path(algo)
        generate_keys(cs, secret_key_path, public_key_path)
        private_key = load_private_keys(secret_key_path)
        public_key = load_public_keys(public_key_path)
    else:
        print("Loading keys...")
        secret_key_path, public_key_path = algo_path(algo)
        private_key = load_private_keys(secret_key_path)
        public_key = load_public_keys(public_key_path)
        cs = init_algo(algo, key=public_key)

    tally = load_and_encrypt_tally(cs, size)
    
    encrypted_vote = load_encrypted_vote("sample_vote/encrypted_vote.pkl")
    tally = tally + encrypted_vote

    decrypt_circuit = init_algo(algo, key=private_key)
    print("Updated encrypted tally:", decrypt_circuit.decrypt(tally))


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    main()