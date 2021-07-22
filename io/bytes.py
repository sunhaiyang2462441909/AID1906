s1 = "hello"  # 字符串
print(s1)

s2 = b"hello"  # 字节串，只有ascii码才能加b转换
print(s2)

s3 = "你好".encode()  # 将字符串转换成字节串
print(s3)

# 所有字符串都能转换成字符串
# 但是并不是所有的字节串都能转换成字符串

# 字节串 转换为 字符串
print(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode())
