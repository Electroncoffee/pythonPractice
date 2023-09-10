a = 10
b = 10.5
c = "큰따옴표에선 '작은따옴표를"
d = '작은따옴표에선 "큰따옴표를 명령어없이 사용가능하며'
e = "이스케이프 코드를 써도 상관없다.\"haha\""
f = """여러줄을
저장할땐
따옴표를 3개로 묶기"""
g = "phthon"
print(a)
print(b)
print(c)
print(d)
print(e)
print("문자열을 +로 합칠 수 있다." + "이렇게")
print(g * 2 + "문자열을 곱셈으로 반복출력 가능하다")
print(len(g))
print(g[0] + g[-0] + g[-1])
print(g[0:4] + g[4:6] + "1")
print(g[:2] + g[2:] + "2")
print(g[:] + "3")
print("I'm studying %s" % g)
print("%d일이 지났습니다." % a)
print("%d일 동안 %s를 공부중" % (a, g))
