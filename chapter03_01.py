# Chapter03_01
# 숫자형

# 파이썬에서 지원하는 자료형
"""
int: 정수
float: 실수
complex: 복소수
bool: 불린. Boolean(True, False)
str: 문자열(시퀀스: 반복을 처리할 수 있고, 순서가 있는 것)
list: 리스트(시퀀스)
tuple: 튜플(시퀀스)
set: 집합
dict: 사전
"""

# 데이터 타입
str1 = "Python"
bool = True
str2 = 'Anaconda'
float_v = 10.0    # 10 != 10.0
int_v = 7
dict = {
    "name": "Machine Learning",     # name과 version을 key라고 함
    "version": 2.0
}
list = [str1, str2] # 대괄호
tuple1 = (7, 8, 9)  # 소괄호
tuple2 = 1, 3, 5    # 괄호가 없어도 됨
set = {3, 5, 7}     # 중괄호

# 데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(list))
print(type(dict))
print(type(tuple1))
print(type(tuple2))
print(type(set))

# 숫자형 연산자
"""
+: 더하기
-: 빼기
*: 곱하기
/: 나누기
//: 몫
%: 나머지
abs(x): 절대값
pow(x, y): x의 y제곱 -> pow(2,3) == 8
x ** y: x의 y제곱 -> 2 ** 3 == 8
"""

# 정수 선언과 출력
i1 = 77
i2 = -14
big_int = 777777777777777777777777999999999999999999999

print(i1)
print(i2)
print(big_int)
print()

# 실수 선언과 출력
f1 = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

print(f1)
print(f2)
print(f3)
print(f4)
print()

#  연산 실습
i1 = 39
i2 = 939
big_int1 = 12345678901234567890123456789012345678901234567890123456789012345678901234567890
big_int2 = 78978978978978978978978978978978978978978978978978978978978978978978978978978978
f1 = 1.123456712345671234567123456712345671234567123456712345671234567123456712345671234567
f2 = 3.939

print("더하기")
print("i1 + i2:", i1 + i2)
print("f1 + f2:", f1 + f2)
print("big_int1 + big_int2:", big_int1 + big_int2)
print()

print("빼기")
print("i1 - i2", i1 - i2)
print("f1 - f2", f1 - f2)
print("big_int1 - big_int2", big_int1 - big_int2)
print()

print("곱하기")
print("i1 * i2:", i1 * i2)
print("f1 * f2:", f1 * f2)
print("big_int1 * big_int2:", big_int1 * big_int2)
print()

print("나누기")
print("i1 / i2", i1 / i2)
print("f1 / f2", f1 / f2)
print("big_int1 / big_int2", big_int1 / big_int2)
print()

# 형 변환 실습
a = 3.  # 3.0에서 0 생략 가능
b = 6   # 정수
c = .7
d = 12.7

print('a=', type(a), 'b=', type(b), 'c=', type(c), 'd=', type(d))   # 타입 출력
print()

# 형 변환
print(float(b))     # int b를 float b로 바꿈
print(int(c))
print(int(a))
print(int(d))
print(int(True))    # True: 1, False: 0
print(float(False))
print(complex(3))   # 복소수 (실수부 + 허수부)
print(complex('3')) # 문자열 3을 입력해도 파이썬은 문자형을 숫자형으로 알아서 바꿔줌
print(complex(False)) # 허수부만 출력
print()

# 수치 연산 함수 
print(abs(-7))      # 절대값을 돌려줌

x, y = divmod(100, 8)   # 100을 8로 나눈 후, x: 몫 12, y: 나머지 4
print(x, y)

print(pow(2,10))    # 거듭제곱
print(2 ** 10)
print()

# 외부 모듈
import math     # math 라이브러리를 불러옴

print(math.pi)  # 원주율
print(math.log10(100)) # log 함수
print(math.cos(0))     # cos 0
print(math.ceil(5.1))  # x 보다 큰 수 중에서 가장 작은 정수