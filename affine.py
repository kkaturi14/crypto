# 확장 유클리드 알고리즘 (모듈러 역원 계산용)
def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

# 모듈러 역원 구하기 (a와 26이 서로소여야 함)
def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError("역원이 존재하지 않음")
    return x % m

# 암호화: E(x) = (a·x + b) mod 26
def affine_encrypt(text, a, b):
    result = []
    for ch in text:
        if ch.isalpha():  # 알파벳이면 암호화
            base = ord('A') if ch.isupper() else ord('a')
            x = ord(ch) - base
            y = (a * x + b) % 26
            result.append(chr(y + base))
        else:  # 알파벳이 아니면 그대로 둠
            result.append(ch)
    return ''.join(result)

# 복호화: D(y) = a⁻¹·(y - b) mod 26
def affine_decrypt(text, a, b):
    result = []
    inv_a = modinv(a, 26)  # a의 역원
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            y = ord(ch) - base
            x = (inv_a * (y - b)) % 26
            result.append(chr(x + base))
        else:
            result.append(ch)
    return ''.join(result)

# 실행 예시
plain = "Hello world!"
a, b = 5, 8  # 키 값
cipher = affine_encrypt(plain, a, b)
print("암호문:", cipher)
print("복호문:", affine_decrypt(cipher, a, b))
