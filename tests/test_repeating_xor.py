# section is souly responsible for allowing tests to utilize src/ files
import sys, os
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), "../src/"
        )
    )
)

import unittest
from vigenere import *
print(f"[*] Executing {os.path.basename(__file__)}...")

class Test_Repeating_XOR(unittest.TestCase):
    def test_big_m_little_k(self):
        m = "Attack at dawn!"
        k = "26b623"
        e, _ = encrypt(m, k)
        self.assertEqual(
            e.hex(),
            "67c25747d54806d75706d24251d802",
            "Encryption failed!"
        )
        
    def test_big_k_little_m(self):
        m = "Golang"
        k = "e8f2d25b2cbb35089cd6e860b045f7"
        e, _ = encrypt(m, k)
        self.assertEqual(
            e.hex(),
            "af9dbe3a42dc",
            "Encryption failed!"
        )
    
    def test_empty_m(self):
        m = ""
        k = "e8f2d25b2cbb35089cd6e860b045f7"
        e, _ = encrypt(m, k)
        self.assertTrue(
            len(e.hex()) == 0,
            "Encryption failed!"
        )
    
    def test_m_with_multi_byte_char(self):
        m = "Café"
        k = "b855b2"
        e, _ = encrypt(m, k)
        self.assertEqual(
            e.hex(),
            "fb34d47bfc",
            "Encryption failed!"
        )

    """
    Arbitrary non-text bytes passed directly
    to the byte-oriented core function
    """
    def test_non_text_bytes(self):
        res_bytes = xor_repeating(
            b"\x00\x01\x68\x65",
            bytes.fromhex("2436d9")
        )
        self.assertEqual(
            res_bytes.hex(),
            "2437b141",
            "Encryption failed!"
        )

    """
    This particular cipher should not perform silent actions
    that may alter the data (reducing integrity)
    """
    def test_whitespace_preserve(self):
        m = "hello\nworld"
        res = xor_repeating(
            bytes.fromhex("030015070a731c0a0b0701"),
            bytes.fromhex("6b6579")
        ).decode("utf-8")

        self.assertTrue(res == m, "Failed to preserve white-space (new-lines)!")
        
        m = "hello world"
        res = xor_repeating(
            bytes.fromhex("030015070a591c0a0b0701"),
            bytes.fromhex("6b6579")
        ).decode("utf-8")

        self.assertTrue(res == m, "Failed to preserve white-space!")

if __name__ == '__main__':
    unittest.main()