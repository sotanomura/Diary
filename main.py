from diaries.DiarySample import DiarySample
from diaries.KimuraDiary import KimuraDiary
from diaries.MatsudoDiary import MatsudoDiary
from diaries.GomamonoDiary import GomamonoDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(), 
    MatsudoDiary(),
    KimuraDiary(),
    AsaiDiary(),
    GomamonoDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()