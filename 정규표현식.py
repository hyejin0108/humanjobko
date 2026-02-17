import re

p = r"hello\n"
s = "hello\n world!"
re.findall(p, s)
re.sub(pattern = p, repl = "hi", string= s)

#%% 문자의 집합
pattern = r"[cehr]at" # cat,eat,hat,rat
pattern = r"[0-9a-Z]" # 0~9, a~z, A~Z
pattern = r"[A-G]열 [1-6]번"
# [az-] [a\-z] a, z, -

# 차집합 [^0]
pattern = r"[^0-9]" # 0-9 제외
pattern = r"[^0]"
s = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10"
print(re.findall(pattern, s))

# \d 숫자 [0-9]
# \D 숫자 제외 [^0-9]
# \w 문자(word) [a-zA-Z0-9_]
# \W 문자 제외 [^a-zA-Z0-9_]
# \s 공백 [ \t\n\r\f\v]
# \S 공백 제외 [^ \t\n\r\f\v]

print(re.findall(r'\D', "아무말0이나10해보기99"))

# . \n을 제외한 모든 문자
# flag=re.DOTALL \n포함
print(re.findall(r".", "모든 문자를 의미한다.\n빼고"))

# ab? b가 있거나 없는 문자 a or ab
print(re.findall(r"hi?", "hi 또는 h hello~"))

# hi* h, hi, hii, hiii, hiii ... hiiiiiiiii*
# hi+ hi, hii, hiii, hiiii, ...., hiiiiiiiiiiii+

print(re.findall(r"hi*", "a h hi hii hiii"))
print(re.findall(r"hi+", "a h hi hii hiii"))

# {a} 반복 횟수 지정
# {a} a회 {a,A} a~A회 반복 {a,} a회 이상 {,A} A회 이하 반복

print(re.findall(r"hi{2}", "h hi hii hiii"))
print(re.findall(r"hi{1,2}", "h hi hii hiii"))
print(re.findall(r"hi{3,}", "h hi hii hiii hiiii"))
print(re.findall(r"hi{,3}", "h hi hii hiii hiiii hiiiiii"))

