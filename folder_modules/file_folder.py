# 모듈 참조
import os
import sys

print("운영체제 이름조회:", sys.platform)

# 현재 폴더 내의 하위 항목들의 이름을 리스트로 반환
# ./ , .은 현재 폴더 의미
ls = os.listdir("./")
print("현재폴더:", ls)

# 상위 폴더  ../
top_ls = os.listdir("../")
print("상위폴더:", top_ls)

# exists 파일이 존재하는지 확인 , 상대경로인 경우 현재 소스파일 기준
k = os.path.exists("./hello")
print(k)

# 절대경로 확인 -> 존재하지 않더라도 경로값은 확인 가능
print(os.path.abspath("./hello"))

# 폴더의 생성과 삭제
if os.path.exists("./hello") == False:
    os.mkdir("./hello")
    print("hello 폴더를 생성했습니다.")
else:
    os.rmdir("./hello")
    print("hello 폴더를 삭제했습니다.")

# 파일이나 폴더 검색
import glob as gl

# glob: 경로 지정을 포함하는 문자열인 pathname에 일치하는 경로 이름의 비어있을 수 있는 리스트 반환
# glob.glob(pathname, *, recursive=False)¶
ls = gl.glob("*")  # 현재 폴더의 모든 항목
print("현재폴더의 모든 항목:", ls)

ls_ipynb = gl.glob("*.ipynb")  # 현재 폴더의 ipynb 파일들
print("현재폴더의 ipynb 파일들:", ls_ipynb)

ls = gl.glob("*2*")  # 현재 폴더의 이름에 2가 포함된 모든 항목
print("현재폴더의 이름에 2가 포함된 모든 항목:", ls)


# 폴더 트리 생성 및 삭제 ,고수준 파일 연산
import shutil

if os.path.exists("python") == False:
    # exist_ok=True -> 이미 존재하더라도 에러 발생 안함
    os.makedirs("python/test/hello/world", exist_ok=True)
    print("python 폴더 트리를 생성했습니다.")
else:
    shutil.rmtree("python")
    print("python 폴더 트리를 삭제했습니다.")
