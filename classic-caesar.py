def caesar_cipher_encrypt(text, key):
  """
  시저 암호로 텍스트를 암호화합니다.
  text: 암호화할 평문 (문자열)
  key: 암호화 키 (정수)
  """

  encrypted_text  = ""
  for char in text:
    if 'a' <= char <= 'z':
      start = ord('a')
      encrypted_char_code =(ord(char) - start + key) % 26 + start 
      encrypted_text += chr(encrypted_char_code)
    elif 'A' <= char <= 'Z':
      start = ord('A')
      encrypted_char_code = (ord(char) - start + key) % 26 + start
      encrypted_text += chr(encrypted_char_code)
    else:
      encrypted_text += char
  return encrypted_text
    

def caesar_cipher_decrypt(text, key):
    """
    시저 암호로 암호화된 텍스트를 복호화합니다.
    암호화 함수와 동일한 로직을 사용하지만, 키를 빼는 방식으로 동작합니다.
    text: 복호화할 암호문 (문자열)
    key: 암호화 시 사용된 키 (정수)
    """
    decrypted_text = ""
    for char in text:
        if 'a' <= char <= 'z':
            start = ord('a')
            decrypted_char_code = (ord(char) - start - key) % 26 + start
            decrypted_text += chr(decrypted_char_code)
        elif 'A' <= char <= 'Z':
            start = ord('A')
            decrypted_char_code = (ord(char) - start - key) % 26 + start
            decrypted_text += chr(decrypted_char_code)
        else:
            decrypted_text += char
    return decrypted_text



plain_text = "Hello, Caesar Cipher!"
key = 6 

# 암호화
cipher_text = caesar_cipher_encrypt(plain_text, key)
print(f"평문: {plain_text}")
print(f"암호화된 텍스트: {cipher_text}")

# 복호화
decrypted_text = caesar_cipher_decrypt(cipher_text, key)
print(f"복호화된 텍스트: {decrypted_text}")
