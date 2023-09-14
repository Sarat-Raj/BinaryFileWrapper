import subprocess
import sys
import binascii

def ascii_to_hex(ascii_text):
    # Convert ASCII text to bytes
    ascii_bytes = ascii_text.encode('utf-8')

    # Convert bytes to hex-encoded text
    hex_text = binascii.hexlify(ascii_bytes).decode('utf-8')
    
    return hex_text



def mothership_wrapper(key, plaintext_hex):
    try:
        # Encode the plaintext as bytes
        plaintext_bytes = plaintext.encode('utf-8')

        # Run the mothership binary and pass the plaintext as input
        process = subprocess.Popen(['./mothership', key, plaintext_hex], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(input=plaintext_bytes)
        
        # Check for errors
        if process.returncode != 0:
            print("Error:", stderr.decode('utf-8'))
            return None

        # Convert the output (ciphertext) to a hexadecimal string
        ciphertext_hex = stdout.hex()
        
        return ciphertext_hex
    except Exception as e:
        print("An error occurred:", str(e))
        return None

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py arg1 arg2")
        sys.exit(1)
    key = sys.argv[1]
    plaintext = sys.argv[2]
    plaintext_hex = ascii_to_hex(plaintext,ascii)
    ciphertext = mothership_wrapper(key, plaintext_hex)
    
    if ciphertext:
        print("Hex-encoded ciphertext:", ciphertext)


