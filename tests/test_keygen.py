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
from vigenere import key_gen, valid_hex
print(f"[*] Executing {os.path.basename(__file__)}...")

class Test_Keygen(unittest.TestCase):
    def setUp(self):
        self.l = 2
        self.key = key_gen(self.l)
    
    def test_key_length(self):
        self.assertEqual(
            len(self.key), 2 * self.l,
            "Key does not meet the constraint of being 2*L in length!"
        )

    def test_key_fmt(self):
        self.assertTrue(
            valid_hex(self.key),
            "Key contains invalid hexademinal characters!"
        )

if __name__ == '__main__':
    unittest.main()