# Secure Key Management System (KMS)

This project demonstrates a Secure Key Management System that integrates symmetric key distribution, Diffie–Hellman key exchange, and a simulated Public Key Infrastructure (PKI). The system is implemented in Python without the use of external libraries.

## Files

- **kms_system.py**  
  The main interface that integrates all modules and provides a menu-driven system for operations.

- **dh_exchange.py**  
  Implements the Diffie–Hellman key exchange protocol with certificate validation via the PKI module.

- **kdc.py**  
  Handles the generation, storage, distribution, and revocation of symmetric keys using file-based JSON storage.

- **pki.py**  
  Simulates a Public Key Infrastructure for issuing, validating, and revoking digital certificates using JSON files.

## How to Run

1. Ensure Python 3 is installed.
2. Clone the repository.
3. Open a terminal in the project directory.
4. Run the main interface with:  

5. Follow the on-screen menu prompts to perform key exchange, key distribution, certificate issuance, or revocation.

## Overview

- **Diffie–Hellman Key Exchange:**  
Establishes a shared secret between two parties after validating their digital certificates.

- **Centralized Key Distribution (KDC):**  
Generates a 256-bit symmetric key using OS-level randomness, stores it securely, and supports key revocation.

- **Public Key Infrastructure (PKI):**  
Simulates certificate issuance, validation, and revocation to authenticate entities during cryptographic operations.

## License

This project is for educational purposes and is free to use.

## Acknowledgments

Special thanks to everyone who supported and contributed to this project.
