from diaries.DiarySample import DiarySample
from diaries.MatsudoDiary import MatsudoDiary
from diaries.KimuraDiary import KimuraDiary
from diaries.AsaiDiary import AsaiDiary
from diaries.GomamonoDiary import GomamonoDiary
from diaries.MasakiDiary import MasakiDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(), 
    MatsudoDiary(),
    KimuraDiary(),
    AsaiDiary(),
    GomamonoDiary(),
    MasakiDiary()
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()