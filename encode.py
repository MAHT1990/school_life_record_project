from urllib import parse

# Encoding을 확인하기위한 임시파일이다.
# 기능이 완성되면 삭제한다.

encode = parse.quote('환')
encode_c = parse.quote(encode)
print(encode)
print(encode_c)
decode = parse.unquote('%25ED%2599%2598')
decode_c = parse.unquote(decode)
print(decode)
print(decode_c)
print(type(decode))
print(type(decode_c))
