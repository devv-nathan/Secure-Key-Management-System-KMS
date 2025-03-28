# kms_system.py
# Integrated Secure Key Management System (KMS)
# This module ties together the key distribution system, Diffie-Hellman key exchange,
# and PKI functionalities including certificate issuance and revocation.

from dh_exchange import diffie_hellman
from kdc import distribute_key, revoke_key
from pki import issue_certificate, revoke_certificate

def main():
    print("=== Secure Key Management System (KMS) ===")
    print("Select an option:")
    print("1. Diffie-Hellman Key Exchange")
    print("2. Distribute Symmetric Key")
    print("3. Issue Digital Certificate (PKI)")
    print("4. Revoke Digital Certificate (PKI)")
    print("5. Revoke Symmetric Key")
    print("6. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-6): ")
        if choice == "1":
            diffie_hellman()
        elif choice == "2":
            entity = input("Enter the entity name for symmetric key distribution: ")
            distribute_key(entity)
        elif choice == "3":
            entity = input("Enter the entity name for certificate issuance: ")
            public_key = input("Enter the public key for the entity: ")
            issue_certificate(entity, public_key)
        elif choice == "4":
            entity = input("Enter the entity name for certificate revocation: ")
            revoke_certificate(entity)
        elif choice == "5":
            entity = input("Enter the entity name for symmetric key revocation: ")
            revoke_key(entity)
        elif choice == "6":
            print("Exiting the KMS. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
