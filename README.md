# Repeating-Key XOR
## 1. Program Information
### 1.1 CLI Interfaces
Below depicts terminal examples of how to use each mode (keygen,encrypt,decrypt).
```bash
# if xor_vigenere does not have executable bit
chmod +x ./xor_vigenere

./xor_vigenere keygen -l 3
./xor_vigenere encrypt -t hello -k 6b6579
./xor_vigenere decrypt -e 030015070a -k 6b6579
```

Below depicts the binary help page, depicting all possible args/options and
their respective meaning.
```console
usage: xor_vigenere [-h] [-l LENGTH] [-k KEY] [-t TEXT] [-e CIPHERTEXT]
                    {keygen,encrypt,decrypt}

positional arguments:
  {keygen,encrypt,decrypt}
                        What mode the program runs in

options:
  -h, --help            show this help message and exit
  -l LENGTH, --length LENGTH
                        Length of Key to be generated
  -k KEY, --key KEY     Value of Key
  -t TEXT, --text TEXT  plain-text message (UTF-8)
  -e CIPHERTEXT, --ciphertext CIPHERTEXT
                        cipher-text message (Hexadecimal)
```

### 1.1 Running Test-Suite
If you are within the root of the project:
```console
python3 -m unittest discover -s ./tests/
```
Or you can run it from within the tests directory:
```console
cd tests
python3 -m unittest discover
```
This is the first time I've tried setting up a test-suite with Python, I'm used to C/C++. There are definitely better ways
to setup a test-suite through Python.

## 2. Mathematic Theory
### 2.1 Proving $Dec_k(Enc_k(m)) = m$
Let $\mathbb{B}=\{0,1,\ldots,255\}$ denote the set of byte values. The message space is $\mathbb{B}^*$, including the empty string,
and the key space is $\mathbb{B}^+$, excluding the empty string. For a message $m=m_0m_1\ldots m_{n-1}$ and key $k=k_0k_1\ldots k_{\ell-1}$,
encryption returns a ciphertext $c=c_0c_1\ldots c_{n-1}$ of the same length, where

$$
Enc_k(m) = c_i=m_i\oplus k_{i\bmod \ell}
\qquad\text{for }0\leq i<n.
$$

Lets a computed ciphertext $c$ and compute $Enc_k(c)$. We can call the result $c'$, we can observe that

$$
Enc_k(c) = c'_i=c_i\oplus k_{i\bmod \ell}
\qquad\text{for }0\leq i<n.
$$
