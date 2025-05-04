from util import *
import multiprocessing

def main():
    args = parse_arg_client()
    algo = args.algo
    size = args.size
    print(f"Algorithm choice: {algo}, Number of candidates: {size}")

    public_key_path = algo_path(algo)[1]
    public_key = load_public_keys(public_key_path)
    cs = init_algo(algo, key=public_key)

    vote = get_user_vote(size)
    encrypted_vote = cs.encrypt(vote)
    save_encrypted_vote(encrypted_vote, "sample_vote/encrypted_vote.pkl")

if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    main()