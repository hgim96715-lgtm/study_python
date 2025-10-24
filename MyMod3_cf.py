
from mylibrary import MyMod3

print(MyMod3.my_calc.plus(30, 15))
print(MyMod3.my_calc.minus(30, 15))

# 별칭적용
from mylibrary import MyMod3 as MyObject
print("별칭적용:", MyObject.my_calc.plus(30, 15))
print("별칭적용:", MyObject.my_calc.minus(30, 15))

# 모듈 이름 없이 함수 직접 접근 
from mylibrary.MyMod3 import my_calc
print("직접접근:",my_calc.plus(30, 15), my_calc.minus(30, 15))