import subprocess
import sys
import binascii

def ascii_to_hex(ascii_text):
    # Convert ASCII text to bytes
    ascii_bytes = ascii_text.encode('utf-8')
    print("ascii_bytes", ascii_bytes)

    # Convert bytes to hex-encoded text
    hex_text = binascii.hexlify(ascii_bytes).decode('utf-8')
    print("hex_text", hex_text)

    #hex_text = binascii.hexlify(ascii_text).decode('utf-8')
    
    return hex_text



def mothership_wrapper(key, plaintext_hex):
    try:
        # Encode the plaintext as bytes
        plaintext_bytes = plaintext.encode('utf-8')
        print(type(plaintext_bytes))
        print(type(plaintext))
        # Run the mothership binary and pass the plaintext as input
        process = subprocess.Popen(['./mothership', '--key', key, '--plaintext',plaintext_bytes], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(input=plaintext_bytes)
        print("stdout",stdout)
        
        # Check for errors
        if process.returncode  != 0:
            print("Error:", stderr.decode('utf-8'))
            return None

        # Convert the output (ciphertext) to a hexadecimal string
    
        
        ciphertext_hex = stdout.decode('utf-8')
        print("ciphertext_hex",ciphertext_hex)
        
        return ciphertext_hex
    except Exception as e:
        print("An error occurred:", str(e))
        return None

def hex_to_ascii(hex_text):
    try:
        # Convert hex-encoded text to bytes
        hex_bytes = bytes.fromhex(hex_text)
        
        # Decode bytes to ASCII text
        ascii_text = hex_bytes.decode('utf-8')
        #ascii_text = hex_text.decode('utf-8')

        return ascii_text
    except Exception as e:
        print("An error occurred:", str(e))
        return None

def decrypt_with_mothership(key, decrypt_ciphertext_hex):
    try:
        
        d_ciphertext = decrypt_ciphertext_hex.encode('utf-8')
        #d_ciphertext_hex = d_ciphertext.hex()
        #print("d_ciphertext_hex",d_ciphertext_hex)
        print(type(d_ciphertext))
        #print(type(d_ciphertext_hex))
        print(type(decrypt_ciphertext_hex))

        print("key",key)
        # Run the mothership binary with the --key and hex-encoded ciphertext
        command = ['./mothership', '--key', key, '--plaintext', d_ciphertext]
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(input=decrypt_ciphertext_hex)
        print("output decode:stdout",stdout)
        
        # Check for errors
        if process.returncode != 0:
            print("Error:", stderr.decode('utf-8'))
            return None

        # Convert the output (plaintext) from hex to ASCII
        
        decrypt_plaintext_hex = stdout.decode('utf-8')
        print("decrypt_plaintext_hex", decrypt_plaintext_hex)
        plaintext_ascii = hex_to_ascii(decrypt_plaintext_hex)
    
        print("plaintext_ascii",plaintext_ascii)
        
        return plaintext_ascii
    except Exception as e:
        print("An error occurred:", str(e))
        return None

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python script.py arg1 arg2")
        sys.exit(1)
    key = sys.argv[1]
    plaintext = sys.argv[2]
    decode_flag = sys.argv[3]
    plaintext_hex = ascii_to_hex(plaintext)
    print(plaintext, plaintext_hex)
    ciphertext = mothership_wrapper(key, plaintext_hex)
    
    if ciphertext:
        print("Cipher Text is")
        print(ciphertext)

        
    if decode_flag=="decode":
        print("inside decode")
        decode_text = decrypt_with_mothership(key, ciphertext)
        print(decode_text)
    else: print("No Decode")


