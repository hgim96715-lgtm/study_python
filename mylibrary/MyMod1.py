# 함수를 포함하는 모듈

def plus(a,b):
    return a + b

def minus(a,b):
    return a - b


# 이 파일을 직접 실행 했을 때만 작동하는 테스트 코드 
if __name__ == "__main__": # 이 한줄은 매우 중요 변하지 않는 문법, 테스트 코드 작성시 꼭 기억할 것
    print(plus(10,20))
    print(minus(10,20))