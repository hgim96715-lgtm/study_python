# MyMod1 참조
from mylibrary import MyMod1

# 참조한 파일에 정의된 함수는 `파일이름.함수명` 형식으로 접근
print(MyMod1.plus(3, 4))


# 별칭 적용 ->`별칭이름.함수명` 형식으로 접근
from mylibrary import MyMod1 as mm1
print("별칭적용:",mm1.plus(3, 4))
print("별칭적용:",mm1.minus(3, 4))


# 모듈 이름 없이 함수 직접 접근 -> 단, import한 함수 외에는 접근 불가(에러발생)
from mylibrary.MyMod1 import plus
from mylibrary.MyMod1 import minus

print("직접접근:",plus(3, 4))
print("직접접근:",minus(3, 4))