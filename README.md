
# JSON Web Token Manager

JSON Web Token Manager is a Python-based tool that allows users to generate, verify, and manage JWTs (JSON Web Tokens) using RSA256 encryption. This project provides a command-line interface (CLI) with interactive and scriptable options.

## Features

- **Generate JWTs** with custom payload data.
- **Verify JWTs** to ensure authenticity and validity.
- **Use RSA key pairs** for signing and verification.
- **Interactive CLI** for manual input.
- **Command-line options** for automation.

## Requirements

Before running the script, make sure you have the following:

- Python 3.6+
- Virtual environment (recommended)
- Required dependencies installed

### Installing Dependencies

To install the required dependencies for this project, run:

```sh
pip install -r requirements.txt
```

The `requirements.txt` file contains the necessary packages for the project, and this command will install them into your environment.

### Generating `requirements.txt`

If you have added new dependencies or want to regenerate the `requirements.txt` file to reflect the current state of your virtual environment, use the following command:

```sh
pip freeze > requirements.txt
```

This command will create or update the `requirements.txt` file with the exact versions of all installed Python packages in your current environment. The file will look like this:

```
flask==2.1.1
requests==2.27.1
numpy==1.1.4
```

Once the `requirements.txt` file is generated, you can share it with others or use it to recreate the same environment with the exact package versions.

### Using `requirements.txt` on Another Machine

To recreate the same environment on another machine, first set up a virtual environment, then install the dependencies listed in the `requirements.txt` file by running:

```sh
pip install -r requirements.txt
```

This ensures that all dependencies are installed with the exact versions specified, maintaining consistency across different setups.

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/valorisa/json-web-token-manager.git
   cd json-web-token-manager
   ```

2. Set up a virtual environment:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

### 1. Generate RSA Keys

Before generating or verifying JWTs, you need to create RSA keys:

```sh
python jwt_manager.py --generate-keys
```

This will create:
- `private.pem` (used for signing JWTs)
- `public.pem` (used for verifying JWTs)

### 2. Generate a JWT

You can generate a JWT with the following command:

```sh
python jwt_manager.py --generate --subject "1234567890" --name "John Doe" --admin True
```

The generated token will be displayed and saved in `jwt_token.jwt`.

### 3. Verify a JWT

To verify a JWT, use:

```sh
python jwt_manager.py --verify --token "your_jwt_here"
```

Alternatively, if you saved the JWT in `jwt_token.jwt`, you can run:

```sh
python jwt_manager.py --verify --file jwt_token.jwt
```

### 4. Interactive Mode

Run the script without arguments to use the interactive menu:

```sh
python jwt_manager.py
```

It will provide options to generate JWTs, verify them, and manage RSA keys.

## Example Output

Generating a JWT:

```sh
$ python jwt_manager.py --generate --subject "1234567890" --name "John Doe" --admin True
JWT generated successfully:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
```

Verifying a JWT:

```sh
$ python jwt_manager.py --verify --token eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Token is valid. Payload:
{
    "sub": "1234567890",
    "name": "John Doe",
    "admin": true,
    "iat": 1739220356,
    "exp": 1739223956
}
```

## Notes

- The script uses **RS256 (RSA Signature with SHA-256)** for signing and verifying tokens.
- Expiry time is automatically set when generating a JWT.
- Keep `private.pem` secure, as it is used to sign tokens.

## License

This project is licensed under the MIT License.

## Author

Maintained by [valorisa](https://github.com/valorisa).^
