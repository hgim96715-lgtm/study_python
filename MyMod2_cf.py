# MyMod2 참조

from mylibrary import MyMod2

mem=MyMod2.Member("파이썬학생","leekh4232@gmail.com")

# 별칭적용
from mylibrary import MyMod2 as User

mem=User.Member('파이썬학생','leekh4232@gmail.com')
print("-----별칭적용----")
mem.view_info()

# 모듈 이름 없이 클래스 직접 접근 -> 단, import한 클래스 외에는 접근 불가(에러발생)
from mylibrary.MyMod2 import Member 
mem=Member('파이썬학생','leekh4232@gmail.com')
print("----직접접근-----")
mem.view_info()