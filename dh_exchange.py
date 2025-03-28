# dh_exchange.py
# Diffie-Hellman Key Exchange Module 
# This module simulates certificate validation before performing the key exchange.

import math
from pki import check_certificate

def diffie_hellman():
    print("\n--- Diffie-Hellman Key Exchange ---")
    
    # Simulate certificate validation for both parties
    print("Validating certificates for Alice and Bob...")
    alice_cert_valid = check_certificate("Alice")
    bob_cert_valid = check_certificate("Bob")
    
    if not (alice_cert_valid and bob_cert_valid):
        print("Certificate validation failed. Aborting key exchange.\n")
        return

    # Input parameters for Diffie-Hellman
    q = int(input("Enter a prime number (q): "))
    a = int(input("Enter a primitive root (a): "))
    Xa = int(input("Enter the private key of Alice: "))
    Xb = int(input("Enter the private key of Bob: "))
    
    # Compute public keys using Python's built-in pow() for modular exponentiation
    Ya = pow(a, Xa, q)
    Yb = pow(a, Xb, q)
    
    print("\nPublic key of Alice:", Ya)
    print("Public key of Bob:", Yb)
    
    # Compute shared secret keys for both parties
    Ka = pow(Yb, Xa, q)
    Kb = pow(Ya, Xb, q)
    
    print("\nShared key computed by Alice:", Ka)
    print("Shared key computed by Bob:", Kb)
    print("--- End of Diffie-Hellman Exchange ---\n")

if __name__ == "__main__":
    diffie_hellman()
