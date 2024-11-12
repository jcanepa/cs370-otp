# TOTP and QR Code Generator for Google Authenticator

This application generates Time-Based One-Time Passwords (TOTPs) compatible with Google Authenticator. It also generates QR codes that can be scanned into the Google Authenticator app, allowing for a 2-factor authentication setup.

The program includes:
- QR code generation for Google Authenticator.
- Continuous OTP generation that matches Google Authenticator codes for 30-second intervals.

## Running the Program

### Step 1: Setup
To keep dependencies isolated, this project uses a Python virtual environment.

Run the following command to set up the virtual environment and install dependencies:

```bash
make install
```
This command creates a virtual environment in a venv directory, then installs the necessary dependencies listed in requirements.txt.

### Step 2: Generate QR Code

To generate a QR code that encodes a TOTP URI compatible with Google Authenticator, run:

```bash
make run ARGS="--generate-qr"
```

This command will create a QR code image named qr.png in the current directory. This QR code can be scanned by Google Authenticator app to add the account for OTP generation.

### Step 3: Generate a Single OTP

To generate an OTP for the current 30-second interval (which will match the OTP in Google Authenticator), run:

```bash
make run ARGS="--get-otp"
```

### Step 4: Clean Up

To delete the virtual environment, use the following command:

```bash
make clean
```
This will remove the venv directory.
