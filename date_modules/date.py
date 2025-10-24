# 현재 시각 조회
import datetime as dt

# 현재 시각을 갖는 객체 가져오는 방법
now_time = dt.datetime.now()

print(f"년도: {now_time.year}")
print(f"월: {now_time.month}")
print(f"날짜: {now_time.day}")
print(f"시간:{now_time.hour}")
print(f"분:{now_time.minute}")
print(f"초:{now_time.second}")
print(f"1/1000초:{now_time.microsecond}")

# 날짜 객체의 성분 추출
# 년,월,일
msg = f"{now_time.year}년 {now_time.month}월 {now_time.day}일 입니다."

# 시, 분,초 추출
msg = f"지금은 {now_time.hour}시 {now_time.minute}분 {now_time.second}초 입니다."

# 현재 요일의 인덱스 조회
# weekday() =>0:월요일 ~ 6:일요일
d = now_time.weekday()
days = ("월", "화", "수", "목", "금", "토", "일")
print("오늘은 %s요일 입니다." % days[d])
