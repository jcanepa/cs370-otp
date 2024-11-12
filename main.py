import sys
import pyotp
import qrcode
import time

user = "jcanepa@oregonstate.com"
issuer = "OSU CS370 OTP App"
secret_key = 'JD3XNKOGKREHUZLZVZHYKUXXBZQSGPNV' # pyotp.random_base32()

def generate_qr(user, issuer, secret):
    # Create the URI expected by Google Authenticator
    uri = pyotp.totp.TOTP(secret).provisioning_uri(name=user, issuer_name=issuer)

    # Generate the QR codex``
    qr = qrcode.make(uri)
    qr.save("qr.png")

    print("QR code saved as 'qr.png'.")

def get_otp(secret):
    totp = pyotp.TOTP(secret)
    while True:
        print("Current OTP:", totp.now())
        time.sleep(30)

def main():
    # Parse command-line arguments
    if len(sys.argv) < 2:
        print("Usage: ./submission --generate-qr or ./submission --get-otp")
        return

    if sys.argv[1] == "--generate-qr":
        generate_qr(user, issuer, secret_key)
    elif sys.argv[1] == "--get-otp":
        get_otp(secret_key)
    else:
        print("Invalid command. Use --generate-qr or --get-otp.")

if __name__ == "__main__":
    main()