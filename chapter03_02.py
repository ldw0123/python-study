# Chapther03-2
# 파이썬 문자형
# 문자형 중요함!

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))   # len: 문자열의 길이를 구하는 함수
print()

# 빈 문자열
str1_t1 = ''     # 빈 문자열 선언 1
str2_t2 = str()  # 빈 문자열 선언 2

print(type(str1_t1), len(str1_t1))  # 길이: 0
print(type(str2_t2), len(str2_t2))  # 길이: 0
print()

# 이스케이프 문자 사용

print("l'Étoile")    # 문자열 안에 작은따옴표를 쓰려면 큰따옴표로 묶어주어야 함
print('l\'Étoile')   # 작은 따옴표로 묶어줄 경우, 작은 따옴표 앞에 역슬래시를 써야 함
print('a \t b')      # \t: tab
print('a \n b')      # \n: 줄 바꿈
print("\000")        # \000: 널 문자
print('a \" b \" c') # \": 따옴표 출력   
print('a \' b \' c')
print()

escape_str1 = "Do you have \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s up?'
print(escape_str2)
print()

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

# Raw String
raw_s = r'D:\python\test'   # 소문자 r: Raw String. 역슬래시 사용하지 않고 역슬래시를 출력

print(raw_s)
print()
