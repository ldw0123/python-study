# Chapter02_02
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
n = 700

# 출력
print('n')
print(n)
print(n+500)
print(n*5)
print(type(n)) # n의 자료형을 출력
print()

# 동시 선언
x = y = z = 5
print(x, y, z)
print()

# 선언과 재선언
var = 75
var = "Change Value" # var 변수의 값을 재선언

print(var)
print(type(var))

# Object Reference
# 변수의 값이 할당 상태일 때
# 1. 타입에 맞는 오브젝트를 생성
# 2. 값을 생성
# 3. 콘솔 출력

# 예 1)
print(300)
print(int(300))

# 예 2)
n = 777
print(n, type(n))

m = n
print(m, n)
print(type(m), type(n))

m = "Dimanche"
print(m, n)
print(type(m), type(n))

# id(identity)확인: 객체의 고유값 확인