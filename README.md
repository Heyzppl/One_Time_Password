TOTP AUTH IMPLEMENTATION
__________________________________________________

REQUIREMENTS:

- Python
- Pip3

SETUP
_____________________________________________

pip3 install -r requirements.txt


HOW TO USE PROGRAM
____________________________________________________________

To generate a QR Code:
    python .\submission.py --generate-qr | (Run this while in the directory of the py file)

    -Will create a QR code image (qr.png) in the same directory
    -Display the secret key

Scan the QR code with the Google Auth app


To generate otp codes:
    python .\submission.py --get-otp | (Run this in the directory the py file is in)









