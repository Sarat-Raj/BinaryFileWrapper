import subprocess
import sys
import binascii

def hex_to_ascii(hex_text):
    try:
        # Convert hex-encoded text to bytes
        hex_bytes = bytes.fromhex(hex_text)
        
        # Decode bytes to ASCII text
        ascii_text = hex_bytes.decode('utf-8')
        
        return ascii_text
    except Exception as e:
        print("An error occurred:", str(e))
        return None

def decrypt_with_mothership(key, ciphertext_hex):
    try:
        # Run the mothership binary with the --key and hex-encoded ciphertext
        command = ['./mothership', '--key', key, '--ciphertext', ciphertext_hex]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        
        # Check for errors
        if process.returncode != 0:
            print("Error:", stderr.decode('utf-8'))
            return None

        # Convert the output (plaintext) from hex to ASCII
        plaintext_ascii = hex_to_ascii(stdout.decode('utf-8').strip())
        
        return plaintext_ascii
    except Exception as e:
        print("An error occurred:", str(e))
        return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python decrypt.py <key> <ciphertext_hex>")
        sys.exit(1)

    key = sys.argv[2]
    ciphertext_hex = sys.argv[1]

    plaintext = decrypt_with_mothership(key, ciphertext_hex)
    
    if plaintext:
        print("Decrypted ASCII plaintext:", plaintext)
