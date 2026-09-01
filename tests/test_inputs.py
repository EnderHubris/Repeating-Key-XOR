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

class Test_Inputs(unittest.TestCase):
    def test_empty_key(self):
        _, err = encrypt("pong", "")
        self.assertFalse(
            len(err) == 0,
            "Empty Key Accepted!"
        )

    def test_odd_len_key_or_e(self):
        _, err = encrypt("pong", "121")
        self.assertFalse(
            len(err) == 0,
            "Odd-Length Key Accepted!"
        )

        _, err = decrypt("2c1", "a2")
        self.assertFalse(
            len(err) == 0,
            "Odd-Length Cipher Accepted!"
        )
    
    def test_hex_chars(self):
        _, err = encrypt("pong", "xy")
        self.assertFalse(
            len(err) == 0,
            "Key containing invalid hex Accepted!"
        )

        _, err = decrypt("xyzs", "a2")
        self.assertFalse(
            len(err) == 0,
            "Cipher containing invalid hex Accepted!"
        )
    
    def test_leading_trailing_whitespace(self):
        # focus on key input
        _, err = encrypt("pong", "  ea2c")
        self.assertFalse(
            len(err) == 0,
            "Key containing leading white-space Accepted!"
        )
        _, err = encrypt("pong", "ea2c  ")
        self.assertFalse(
            len(err) == 0,
            "Key containing trailing white-space Accepted!"
        )

        # focus on cipher input
        _, err = decrypt("  030015070a", "6b6579")
        self.assertFalse(
            len(err) == 0,
            "Cipher containing leading white-space Accepted!"
        )
        _, err = decrypt("030015070a  ", "6b6579")
        self.assertFalse(
            len(err) == 0,
            "Cipher containing trailing white-space Accepted!"
        )

        return
    
    def test_bad_utf8(self):
        _, err = decrypt("aaaaaaaaaaaaaa", "6b6579")
        self.assertFalse(
            len(err) == 0,
            "Allowed invalid utf-8 decoding!"
        )
        return

if __name__ == '__main__':
    unittest.main()