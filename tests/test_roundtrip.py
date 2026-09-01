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

class Test_Roundtrip(unittest.TestCase):
    def test_roundtrip(self):
        m = "Attack at dawn!"
        k = "26b623"

        e, _ = encrypt(m, k)
        d, _ = decrypt(e.hex(), k)

        self.assertTrue(m == d.decode("utf-8"), "Dec(Enc(m,k)) = m failed!")

if __name__ == '__main__':
    unittest.main()