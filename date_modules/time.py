# strftime()
# datetime 객체를 문자열로 반환

import datetime as dt

now_time = dt.datetime.now()
now_str = now_time.strftime("%Y-%m-%d %H:%M:%S")
print(now_str)  # 2025-10-24 15:16:04
print(
    now_time.strftime("%Y년 %m월 %d일 %H시 %M분 %S초")
)  # 2025년 10월 24일 15시 18분 19초

# 특정시각 지정하기
some_time = dt.datetime(2023, 12, 25, 15, 30, 0)  # 년, 월, 일, 시, 분 ,초
print(some_time.strftime("%Y-%m-%d %H:%M:%S"))  # 2023-12-25 15:30:00

#  strptime()
# 문자열을 datetime 객체로 변환 -> 문자열 이랑 포맷이랑 맞아야함! 틀리면 안됨
change_str = "2018년 12월 25일 15시 30분 00초"
change_time = dt.datetime.strptime(change_str, "%Y년 %m월 %d일 %H시 %M분 %S초")
print("strptime:", change_time)

# 존재하지 않는 날짜 에러 발생
# wrong_day = dt.datetime(2018, 12, 32, 0, 0, 0) # 32일은 없음
# print("wrong_day:", wrong_day) #ValueError: day is out of range for month

# replace()
# datetime 객체의 특정 성분 변경, 바꾸고 싶은 성분만 바꿀수 있다.

foo = dt.datetime.now()
print("변경전:", foo.strftime("%Y-%m-%d %H:%M:%S"))
change_foo = foo.replace(year=2020, month=2)
print("변경후:", change_foo.strftime("%Y-%m-%d %H:%M:%S"))


# 두 날짜 간의 차이 계산
# timedelta 객체 활용
# 날짜를 더하거나 뺄 수 있다.
# 두 날짜의 차를 계산하면 timedelta 객체가 반환된다.
dt1 = dt.datetime(2023, 1, 1, 0, 0, 0)
print("dt1:", dt1)  # 2023-01-01 00:00:00
dt2 = dt.datetime(2024, 6, 30, 0, 0, 0)
print("dt2:", dt2)  # 2024-06-30 00:00:00
td = dt2 - dt1
print("날짜 차이:", td)  # 날짜 차이: 546 days, 0:00:00
print("날짜만 추출:", td.days)  # 날짜만 추출: 546
print("날짜를 제외하고 시간,분,초 단위를 모두 초로 합산:", td.seconds)  # 0
print("두날짜의 차이를 초로 환산:", td.total_seconds())  # 47174400.0

# 임의의 timedelta 객체 생성
td = dt.timedelta(days=100, seconds=60)
print("임의의 timedelta:", td)  # 임의의 timedelta: 100 days, 0:01:00
