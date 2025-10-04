import sympy as sp
import math

"key and plaintext length should be a square"
key = 'GYBNQKURP'
plaintext = 'ACT'
enc = ''

def matrixmaker(text):
  n = int(math.sqrt(len(text)))
  vals = [(ord(ch.lower()) - ord('a')) % 26 for ch in text]
  return sp.Matrix(n, n, vals)

def matrixtostring(matrix):
  text = ''
  for col in range(matrix.cols):
    for row in range(matrix.rows):
      v = int(matrix[row, col]) % 26
      text += chr(v + ord('a'))
  return text

def encryption():
  keym = matrixmaker(key)
  plaintextm = matrixmaker(plaintext)
  encm = (keym * plaintextm) % 26
  return matrixtostring(encm)

def decryption(enc_text):
  encm = matrixmaker(enc_text)
  keym = matrixmaker(key)
  inv_key = keym.inv_mod(26)
  decm = (inv_key * encm) % 26
  return matrixtostring(decm)

def bf2x(enc_text):
  encm = matrixmaker(enc_text)
  for a in range(26):
    for b in range(26):
      for c in range(26):
        for d in range(26):
          keym = sp.Matrix([[a, b], [c, d]])
          try:
            inv_key = keym.inv_mod(26)
            dec = (inv_key * encm) % 26
            print(matrixtostring(dec))
          except:
            continue
  return None

enc = encryption()
print("Encrypted text:", enc)

check = decryption(enc)
print("Decrypted text:", check)
