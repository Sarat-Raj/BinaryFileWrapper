import sys
import subprocess
import sys
import binascii
def xor_hex_strings(hex_str1, hex_str2):
    # Convert hex sstrings to integers
    int_value1 = int(hex_str1, 16)
    int_value2 = int(hex_str2, 16)
    
    # Perform XOR operation
    result = int_value1 ^ int_value2
    
    # Convert the result back to a hex string
    hex_result = hex(result)[2:]  # [2:] is used to remove the "0x" prefix
    
    # Ensure the result has the same length as the input hex strings
    max_length = max(len(hex_str1), len(hex_str2))
    hex_result = hex_result.zfill(max_length)
    
    return hex_result

def hex_to_ascii(hex_text):
    try:
        # Convert hex-encoded text to bytes
        hex_bytes = bytes.fromhex(hex_text[:512]).decode('ascii')
        
        # Decode bytes to ASCII text
        #ascii_text = hex_bytes.
        #ascii_text = hex_text.decode('utf-8')

        return hex_bytes
    except Exception as e:
        print("An error occurred:", str(e))
        return None


if __name__ == "__main__":
    for x in range(10):
        try:
            process = subprocess.Popen(['./mothership'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            hex_string1, stderr = process.communicate()
            process = subprocess.Popen(['./mothership'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            hex_string2, stderr = process.communicate()
            #hex_string1 = sys.argv[1]
            #hex_string2 = sys.argv[2]
            result = xor_hex_strings(hex_string1, hex_string2)
            print("Result of XOR:", result)
            print(type(result))
            result_ascii=hex_to_ascii(result)
            print("Result of XOR in Ascii",result_ascii)
        except Exception as e:
            print("An error occurred:", str(e))
            

