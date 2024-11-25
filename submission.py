"""
https://datatracker.ietf.org/doc/html/rfc6238
https://github.com/google/google-authenticator/wiki/Key-Uri-Format
https://pyauth.github.io/pyotp/
"""
import pyotp
import qrcode
import sys
import time

class TOTP:
    def __init__(self):

        # generate a base 32 secret key
        self.secret = pyotp.random_base32()
        # create a TOTP object
        self.totp = pyotp.TOTP(self.secret)

    def generate_qr_code(self):
        # generate a QR code and get a provisioning URI
        uri = self.totp.provisioning_uri()

        print(f"Secret Key: {self.secret}")

        # create a QR code
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )
        qr.add_data(uri)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        img.save("qr.png")
        print("QR code has generated as qr.png")

    def generate_otp(self):
        #GET THE CURRENT TOTP CODE
        return self.totp.now()
    
def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ['--generate-qr', '--get-otp']:
        print("Usage: ./submission [--generate-qr | --get-otp]")
        sys.exit(1)
    
    totp = TOTP()

    if sys.argv[1] == '--generate-qr':
        totp.generate_qr_code()

    elif sys.argv[1] == '--get-otp':
        while True:
            otp = totp.generate_otp()
            print(f"Current OTP: {otp}")
            time.sleep(30 - (time.time() % 30)) 

if __name__ == "__main__":
    main()



