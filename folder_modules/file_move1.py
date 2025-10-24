import os
import shutil
# 폴더 이동 및 복사
if os.path.exists('python'):
    shutil.move('python','../created') 
    print("python 폴더를 상위폴더로 이동+ python->created로 폴더명 변경되었습니다.")

if os.path.exists('../created'):
    shutil.copytree('../created','./copy')
    print("created 폴더가 현재폴더로 copy 폴더명으로 복사되었습니다.")