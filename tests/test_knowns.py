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

class Test_Knowns_Table(unittest.TestCase):
    def setUp(self):
        self.ciphers = [
            "08373128202e6922316927243e2d64",
            "030015070a",
            "a55ba7595ba5"
        ]

        self.keys = [
            "494345",
            "6b6579",
            "a55a"
        ]

        self.plain_hex = [
            "41747461636b206174206461776e21",
            "68656c6c6f",
            "00010203feff"
        ]
    
    def test_known(self):
        for i in range(0, len(self.ciphers)):
            m_bytes = xor_repeating(
                bytes.fromhex(self.ciphers[i]),
                bytes.fromhex(self.keys[i])
            )

            self.assertEqual(
                m_bytes,
                bytes.fromhex(self.plain_hex[i]),
                f"Known Answer {i+1} Failed!"
            )

if __name__ == '__main__':
    unittest.main()
