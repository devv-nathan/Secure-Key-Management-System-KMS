# kdc.py
# Centralized Key Distribution System for symmetric key generation and revocation.
# This module simulates a KDC that generates a 256-bit symmetric key,
# stores it in a simple file-based database, and supports key revocation.

import os
import json

SYMMETRIC_KEY_DB_FILE = "sym_key_db.json"
REVOCATION_LIST_FILE = "sym_revoked.json"

def load_sym_key_db():
    if os.path.exists(SYMMETRIC_KEY_DB_FILE):
        with open(SYMMETRIC_KEY_DB_FILE, "r") as f:
            return json.load(f)
    else:
        return {}

def save_sym_key_db(db):
    with open(SYMMETRIC_KEY_DB_FILE, "w") as f:
        json.dump(db, f, indent=4)

def load_revocation_list():
    if os.path.exists(REVOCATION_LIST_FILE):
        with open(REVOCATION_LIST_FILE, "r") as f:
            return json.load(f)
    else:
        return []

def save_revocation_list(rev_list):
    with open(REVOCATION_LIST_FILE, "w") as f:
        json.dump(rev_list, f, indent=4)

def generate_symmetric_key():
    # Generate a 256-bit symmetric key using os.urandom from the standard library.
    key = os.urandom(32)
    return key.hex()

def distribute_key(entity):
    key = generate_symmetric_key()
    db = load_sym_key_db()
    db[entity] = key
    save_sym_key_db(db)
    print("\n[Key Distribution]")
    print("Distributed symmetric key to entity:", entity)
    print("Key (hex):", key)
    return key

def revoke_key(entity):
    db = load_sym_key_db()
    if entity in db:
        # Mark the key as revoked by moving it to a revocation list
        rev_list = load_revocation_list()
        rev_list.append({entity: db[entity]})
        save_revocation_list(rev_list)
        del db[entity]
        save_sym_key_db(db)
        print("\n[Key Revocation]")
        print("Symmetric key for", entity, "has been revoked.")
    else:
        print("\nNo key found for", entity)

if __name__ == "__main__":
    # Demo key distribution and revocation
    entity = input("Enter entity name for key distribution: ")
    distribute_key(entity)
    action = input("Do you want to revoke the key? (y/n): ")
    if action.lower() == "y":
        revoke_key(entity)
