"""
    1.1 문자열 인코딩이란?
    문자 집합 (charset)
    - 문자 집합은 사용할 수 있는 문자들의 집합을 의미하며 유니코드, ISO-8859, ASCII 등이 해당한다.

    문자열 인코딩 (character encoding)
    - 2진법을 사용하는 컴퓨터가 인간의 언어를 일정한 규칙에 따라 2진수로 변환하는 방식이며, 아스키 코드, EUC-KR, UTF-8, UTF-16, UTF-32 등이 해당 된다. 
    - "유니코드라는 문자집합을 표현하는 문자열 인코딩은 UTF-8, UTF-16, UTF-32가 있다."라고 말하는 것이 정확한 표현
"""
# 2진수를 10진수로 처리
print(f"10진수(01000001)={0b01000001}")

# 2진수를 16진수로 처리
print(f"16진수(01000001={hex(0b01000001)}")

# 2진수를 문자로 처리
print(f"문자(01000001={chr(0b01000001)}")