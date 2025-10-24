import os
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart


# from_addr = "보내는 사람 주소"

# to_addr = "받는사람 주소"

# 제목
subject = "제목입니다."

# 본문
content = """
내용 입니다.
"""
# 첨부파일이 필요 없는 경우
files=['food.jpeg']

# 컨텐츠형식 (plain, html)
content_type = "plain"

# 로그인 계정 이름
# username = "로그인계정 이름"

# 비밀번호
# password = "앱 비밀번호"

# 구글 발송 서버 주소와 포트 (고정값)
smtp = "smtp.gmail.com"
port = 587

# 메일 발송 정보를 저장하기 위한 객체
msg = MIMEMultipart()
msg["Subject"] = subject
msg["From"] = from_addr
msg["To"] = to_addr

msg.attach(MIMEText(content, content_type))

if files:
    for file_item in files:
        if os.path.exists(file_item):
            with open(file_item,"rb") as f:
                basename=os.path.basename(file_item)
                part=MIMEApplication(f.read(),Name=basename)
                part['Content-Disposition']=f'attachment; filename="{basename}"'
                msg.attach(part)

                print(basename,"첨부 완료")
else:
    print("첨부파일이 없습니다.")

mail = SMTP(smtp)
# 메일 서버 접속
mail.ehlo()
# 메일 서버 연동 설정
mail.starttls()
# 메일 서버 로그인
# mail.login(username, password)
# 메일 보내기
# mail.sendmail(from_addr, to_addr, msg.as_string())
# 메일 서버 접속 종료
print("메일 발송 완료")
mail.quit()