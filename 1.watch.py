# 秒単位の時間 S が与えられるので、h:m:sの形式へ
# 変換して出力してください。ここで、hは時間、mは 60 未満の分、sは 60 未満の秒とします。

#s = int(input())
# s = 30000

# m = s / 60

# h = m / 60


# print(str(s))
# print(str(m))
# print(str(h))


s = int(input())
h = s // 3600
m = s % 3600 // 60
s = s % 60
print(f"{h}:{m}:{s}")

#8:20:00
#30000
