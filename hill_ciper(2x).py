import sympy as sp
import math

key = ''
plaintext = ''
enc = None

def pad_text(text, block_size):
  return (text + 'x' * (block_size * block_size))[:block_size * block_size]

def matrixmaker(text):
  n = int(math.sqrt(len(text)))
  vals = [(ord(ch.lower()) - ord('a')) % 26 for ch in text]
  return sp.Matrix(n, n, vals)

def encryption(key, plaintext):
  keym = matrixmaker(key)
  plaintextm = matrixmaker(plaintext)
  enc = (keym * plaintextm) % 26
  return enc

def decrytption(key, enc):
  keym = matrixmaker(key)
  inv_key = keym.inv_mod(26)
  dec = (inv_key * enc) % 26
  return dec

def bf2x(enc):
  for a in range(26):
    for b in range(26):
      for c in range(26):
        for d in range(26):
          keym = sp.Matrix([[a, b], [c, d]])
          try:
            inv_key = keym.inv_mod(26)
            dec = (inv_key * enc) % 26
            recovered = []
            for col in range(dec.cols):
              for row in range(dec.rows):
                v = int(dec[row, col]) % 26
                recovered.append(chr(v + ord('a')))
            print(''.join(recovered))
          except:
            continue
  return None
