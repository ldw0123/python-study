# Chapter02_02
# 파이썬 완전 기초
# 파이썬 변수

# 기본 변수 선언
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
print()

# id(identity)확인: object(객체)의 고유 값 확인
m = 800
n = 655

print(id(m)) # object의 고유 주소 값
print(id(n))
print(id(m) == id(n)) # id의 m과 id의 n이 같은가? 같으면 true, 다르면 false
print() # false

# 같은 오브젝트를 참조
m = 800
n = 800

print(id(m)) 
print(id(n))
print(id(m) == id(n)) 
print() # true

# 다양한 변수 선언
# Camel Case: numberOfCollegeGraduates -> Method를 선언할 때 주로 사용
# Pascal Case: NumberOfCollegeGraduates -> Class를 선언할 때 주로 사용. 별로 좋지 않음 권장X
# Snake Case: number_of_college_graduates -> 변수를 선언할 때 주로 사용. 추천하는 방법

studentGrade = 3    # Camel Case
student_grade = 3   # Snake Case

# 허용하는 변수 선언법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE = 8

# 예약어는 변수명으로 선언 불가능
"""
불가능한 예약어 목록
False, def, if, raise
None, del, import, return
True, elif, in, try
and, else, is, while
as, except, lambda, with
assert, finally, nonlocal, yield
break, for, not	
class, from, or	
continue, global, pass	
"""