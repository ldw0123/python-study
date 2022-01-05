# Chapter02_01
# 파이썬 완전 기초
# print 사용법

# 기본 출력
print('Python Start!')
print("Python Start!")
print('''Python start!''')
print("""Python start!""")

print() # 줄 바꿈

# separator 옵션: 각 요소 사이에 추가함
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('010', '7777', '1234', sep="-")
print('python', 'google.com', sep="@")

print()

# end 옵션: 끝 부분에 추가
print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')

# file 옵션
import sys

print('Learn Python', file=sys.stdout) # 'Learn Python'을 file에 저장하겠다는
print()

# format 사용(d 정수, s 문자열, f 실수)
print('%s %s' % ('one', 'two'))     # %s: 문자열 형식
print('{} {} {}'.format('one', 'two', '3'))     # 형식에 구애받지 않음. {}에는 .format이 함께 옴
print('{1} {0}'.format('one', 'two'))   # 1번째 요소에는 one이 저장, 0번째 요소에는 two가 저장됨
print()

# %s: 문자열 출력하기
print('%10s' % ('nice')) # 총 10자리. 앞의 공백 6자리, 뒤의 텍스트 4자리
print('%10s' % ('Enchanté')) # 앞의 공백 2자리
print('{:>10}'.format('nice'))

print('%-10s' % ('nice')) # 왼쪽부터 글을 채우고 오른쪽을 공백으로 채움
print('%-10s' % ('Enchanté'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice')) # 공백을 _ 로 채움
print('{:$>10}'.format('nice')) # 공백을 $ 로 채움
print('{:^10}'.format('nice')) # 중앙 정렬

print('%5s' % ('Enchanté')) # 5자리가 넘어도 출력
print('%.5s' % ('Enchanté')) # 5자리만 출력
print('{:10.5}'.format('Enchanté')) # 총 10자리의 공간 중 5자리만 출력
print()

# %d: 정수 출력하기
print('%d %d' % (1,2))
print('{} {}'.format(1,2))
print('%5d' % (42)) # 4자리 중 앞에 공백 3자리
print('%5d' % (42424242))
print('{:5d}'.format(42)) # %s와는 다르게 숫자에 d를 붙여서 {:5d}의 형식으로 써야 함
print()

# %f: 실수 출력하기
print('%f' % (3.14159226535)) # 소수점 6자리까지 출력됨
print('%1.8f' % (3.14159226535)) # 정수부 1자리, 소수부 8자리 출력
print('%1.16f' % (3.14159226535))
print('{:f}'.format(3.14159226535))

print('%06.2f' % (3.14159226535)) # 총 6자리. 정수부는 1자리이기 때문에 0으로 2자리를 채우고 나머지를 6자리에 맞게 출력
print('{:06.2f}'.format(3.14159226535))