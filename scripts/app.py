from flask import Flask, request, render_template, jsonify
from util import *
import multiprocessing
import os
import time
import threading

# Default settings
DEFAULT_ALGO = 0 # 0: Paillier, 1: ElGamal, 2: Benaloh
DEFAULT_SIZE = 3  # Number of candidates

# Global variables for encrypted tally
global_tally = None
tally_lock = threading.Lock()  # To prevent race conditions

def initialize_tally():
    """Initialize the global tally at application startup"""
    global global_tally
    
    # Load public key
    _, public_key_path = algo_path(DEFAULT_ALGO)
    public_key = load_public_keys(public_key_path)
    cs = init_algo(DEFAULT_ALGO, key=public_key)
    
    # Start with zero tally
    tally = load_and_encrypt_tally(cs, DEFAULT_SIZE)
    
    global_tally = tally
    print("Global tally initialized")

def create_app():
    app = Flask(__name__)
    multiprocessing.set_start_method('spawn', force=True)
    with app.app_context():
        initialize_tally()

    @app.route('/')
    def index():
        return render_template('index.html', size=DEFAULT_SIZE)

    @app.route('/vote', methods=['POST'])
    def vote():
        global global_tally
        
        candidate = int(request.form.get('candidate', 0))
        size = DEFAULT_SIZE

        # Get algorithm name
        algo_names = {
            0: "Paillier",
            1: "EllipticCurve-ElGamal",
            2: "Benaloh"
        }
        algo_name = algo_names.get(DEFAULT_ALGO, "Unknown")
        
        # Create vote array
        vote = [0] * size
        vote[candidate] = 1
        
        # Load public key and encrypt vote
        _, public_key_path = algo_path(DEFAULT_ALGO)
        public_key = load_public_keys(public_key_path)
        cs = init_algo(DEFAULT_ALGO, key=public_key)
        
        # Measure encryption time
        start_time = time.time()
        encrypted_vote = cs.encrypt(vote)
        encryption_time = time.time() - start_time
        
        # Update global tally with thread safety
        with tally_lock:
            global_tally = global_tally + encrypted_vote
        
        return jsonify({
            "success": True, 
            "message": "Vote recorded",
            "algorithm": algo_name,
            "encrypted_vote": str(encrypted_vote),
            "encrypted_tally": str(global_tally),
            "encryption_time_seconds": round(encryption_time, 3)
        })

    @app.route('/results')
    def results():
        """Display election results (this would be protected in a real system)"""
        algo = DEFAULT_ALGO
        size = DEFAULT_SIZE
        
        # Load keys
        secret_key_path, public_key_path = algo_path(algo)
        private_key = load_private_keys(secret_key_path)
        public_key = load_public_keys(public_key_path)
        
        # Decrypt the tally
        decrypt_circuit = init_algo(algo, key=private_key)
        final_tally = decrypt_circuit.decrypt(global_tally)
        
        return jsonify({"decrypted_tally": final_tally})

    # Admin endpoint to generate keys
    @app.route('/admin/setup', methods=['POST'])
    def setup_keys():
        # This would be protected in a real system
        algo = DEFAULT_ALGO
        
        # Generate keys
        cs = init_algo(algo)
        secret_key_path, public_key_path = algo_path(algo)
        
        # Ensure directories exist
        os.makedirs(os.path.dirname(secret_key_path), exist_ok=True)
        
        generate_keys(cs, secret_key_path, public_key_path)
        return jsonify({"success": True, "message": "Keys generated"})
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()