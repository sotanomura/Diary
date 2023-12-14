from diaries.DiarySample import DiarySample
from diaries.MasakiDiary import MasakiDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), MasakiDiary()]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()