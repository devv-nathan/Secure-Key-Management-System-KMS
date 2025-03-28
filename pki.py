# pki.py
# Public Key Infrastructure (PKI) Simulation Module.
# This module simulates certificate issuance, checking, and revocation
# using file-based storage (JSON) 

import json
import os

CERT_DB_FILE = "cert_db.json"
CRL_FILE = "crl.json"

def load_cert_db():
    if os.path.exists(CERT_DB_FILE):
        with open(CERT_DB_FILE, "r") as f:
            return json.load(f)
    else:
        return {}

def save_cert_db(db):
    with open(CERT_DB_FILE, "w") as f:
        json.dump(db, f, indent=4)

def load_crl():
    if os.path.exists(CRL_FILE):
        with open(CRL_FILE, "r") as f:
            return json.load(f)
    else:
        return []

def save_crl(crl):
    with open(CRL_FILE, "w") as f:
        json.dump(crl, f, indent=4)

def issue_certificate(entity, public_key):
    # Simulate certificate issuance using a dictionary
    cert = {
        "entity": entity,
        "public_key": public_key,
        "status": "valid"
    }
    db = load_cert_db()
    db[entity] = cert
    save_cert_db(db)
    print("\n[Certificate Issuance]")
    print("Issued certificate for entity:", entity)
    return cert

def revoke_certificate(entity):
    db = load_cert_db()
    if entity in db:
        db[entity]["status"] = "revoked"
        save_cert_db(db)
        # Add to Certificate Revocation List (CRL)
        crl = load_crl()
        crl.append(entity)
        save_crl(crl)
        print("\n[Certificate Revocation]")
        print("Certificate for", entity, "has been revoked.")
    else:
        print("\nNo certificate found for", entity)

def check_certificate(entity):
    db = load_cert_db()
    if entity in db and db[entity]["status"] == "valid":
        print("Certificate for", entity, "is valid.")
        return True
    else:
        print("Certificate for", entity, "is not valid or does not exist.")
        return False

if __name__ == "__main__":
    # Demo certificate operations
    issue_certificate("Alice", "AlicePublicKey")
    issue_certificate("Bob", "BobPublicKey")
    check_certificate("Alice")
    revoke_certificate("Alice")
    check_certificate("Alice")
