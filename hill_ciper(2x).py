import sympy as sp
import math

key = 'GYBNQKURP'         # Must be n×n
plaintext = 'ACT'         # Must be length n

def matrixmaker(text, rows, cols):
  vals = [(ord(ch.lower()) - ord('a')) % 26 for ch in text]
  return sp.Matrix(rows, cols, vals)

def matrixtostring(matrix):
  text = ''
  for col in range(matrix.cols):
    for row in range(matrix.rows):
      v = int(matrix[row, col]) % 26
      text += chr(v + ord('a'))
  return text

def encryption():
  n = int(math.sqrt(len(key)))
  keym = matrixmaker(key, n, n)
  plaintextm = matrixmaker(plaintext, n, 1)
  encm = (keym * plaintextm) % 26
  return matrixtostring(encm)

def decryption(enc_text):
  n = len(enc_text)      
  encm = matrixmaker(enc_text, n, 1)
  keym = matrixmaker(key, n, n)
  inv_key = keym.inv_mod(26)
  decm = (inv_key * encm) % 26
  return matrixtostring(decm)

def bf2x(enc_text):
  n = len(enc_text)
  encm = matrixmaker(enc_text, 2, 1)
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
