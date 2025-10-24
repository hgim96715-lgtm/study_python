# 파일 생성 및 삭제 예제2
import os
import shutil

if os.path.exists("hello.txt") == False:
    with open("hello.txt", "w", encoding="utf-8") as f:
        f.write("Hello, World!")
        print("hello.txt 파일이 생성되었습니다.")
    shutil.copy("hello.txt", "world.txt")
    print("hello.txt -> world.txt ")
else:
    os.remove("hello.txt")
    print("hello.txt 파일이 삭제되었습니다.")
    os.remove("world.txt")
    print("world.txt 파일이 삭제되었습니다.              ")
