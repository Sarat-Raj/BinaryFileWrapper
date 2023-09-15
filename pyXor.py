import sys

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



if __name__ == "__main__":
    hex_string1 = sys.argv[1]
    hex_string2 = sys.argv[2]
    result = xor_hex_strings(hex_string1, hex_string2)
    print("Result of XOR:", result)