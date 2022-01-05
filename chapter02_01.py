# Chapter02_01
# 파이썬 완전 기초
# print 사용법

# 기본 출력
print('Python Start!')
print("Python Start!")
print('''Python start!''')
print("""Python start!""")

print()     # 줄 바꿈

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
print('{} {} {}'.format('one', 'two', '3'))     # 형식에 구애받지 않음
print('{1} {0}'.format('one', 'two'))   # 1번째 요소에는 one이 저장, 0번째 요소에는 two가 저장됨
