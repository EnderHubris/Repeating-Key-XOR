import secrets

"""
Returns false if the provided bytes fail to decode using UTF-8 codex
"""
def valid_codex(data: bytes) -> bool:
    try:
        data.decode("utf-8")
        return True
    except ValueError:
        return False

"""
Returns false if the provided hex-string contains invalid hex
and the conversion fails
"""
def valid_hex(h_str: str) -> bool:
    try:
        bytes.fromhex(h_str)
        return True
    except ValueError:
        return False
    
"""
Returns false if the Data String is either:
- empty (no length)
- odd or negative length
- contains invalid hex-chars
- contains leading or trailing white-space
"""
def valid_data(data: bytes, name: str):
    # name arg testing
    acceptable_names = ["cipher","key"]
    if name.lower() not in acceptable_names:
        return False, f"[-] valid_data name argument can only be: {acceptable_names}"

    # length checking
    data_len = len(data)
    if (name.lower() == "key" and data_len <= 0) or data_len % 2 != 0:
        return False, f"[-] Error: Length of {name} must be non-zero postive-even"

    # leading/trailing white-space check
    data_stripped = data.decode().strip()
    if len(data.decode()) != len(data_stripped):
        return False, f"[-] Error: {name} contains leading/trailing white-space"

    # check key or cipher for invalid hex-chars
    if not valid_hex(data.decode("utf-8")):
        return False, f"[-] Error: {name} contains invalid hexadecimal characters"
    
    return True, ""




"""
@interface used for testing
Core Function for Generating a random Hexademinal key-string
of length 2 * length
"""
def key_gen(length: int) -> bytes:
    key = secrets.token_hex(length)
    return key

"""
@interface used for testing
Core Function for XOR Repeating-Key algorithm
"""
def xor_repeating(data: bytes, key: bytes) -> bytes:
    n_data = bytearray()
    data_len = len(data)
    key_len = len(key)

    for i in range(0, data_len):
        n_data.append(data[i] ^ key[i % key_len])

    return bytes(n_data)

"""
@interface used for testing
Encryption method that handles plain-text and hex-string key
and returns the cipher-text in a hex-string
"""
def encrypt(plain: str, key: str):
    ok, err = valid_data(key.encode("utf-8"), "Key")
    if not ok:
        return b"", err

    enc_bytes = xor_repeating(
        plain.encode("utf-8"),
        bytes.fromhex(key)
    )

    return enc_bytes, ""

"""
@interface used for testing
Decryption method that handles the hex-string cipher-text and key
and returns a tuple of the plain-text bytes and decoded utf-8 message
"""
def decrypt(enc: str, key: str):
    key_ok, key_err = valid_data(key.encode("utf-8"), "Key")
    if not key_ok:
        return b"", key_err
    
    enc_ok, enc_err = valid_data(enc.encode("utf-8"), "Cipher")
    if not enc_ok:
        return b"", enc_err

    m_bytes = xor_repeating(
        bytes.fromhex(enc),
        bytes.fromhex(key)
    )

    if not valid_codex(m_bytes):
        return b"", "Cannot UTF-8 Decode retrived bytes!"

    return m_bytes, ""
