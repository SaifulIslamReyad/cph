# fString debugging feature
a: int = 5
b: int = 6
string : str = "hello world"
print(f"line 4 : {a + b = }")
print(f"{a = }")
print(f"{str(a) = }")
print(f"{bool(a) = }")
print(f"{string = }")
print()
# ---------------------
from icecream import ic
n: int = 10_00_000
ic(n)
# n: int = 10,00,000  #cant use this

m: float = 1e9 + 0.010101
print(f"{m:_}")
print(f"{m:,}")
print(f"{m:,.3f}")
print(f"{m:_.0f}")
print()

# ------------------------------------------

text : str = "enter name"
text2 : str = "enter age"
print(f"{text:<20}:")  #adds extra 10 spaces; left align
print(f"{text:20}:")  #adds extra 10 spaces ; default, left align
print(f"{text2:<20}:")  #adds extra 11 spaces  ; 
print(f"{text:>20}:")  # right align
print(f"{text:^20}:") #center align

print(f"{text:#<30}:")
print(f"{text:@>30}:")
print(f"{text:&^30}:")
print()
# ---------------------------------------------

from datetime import datetime
akhon: datetime = datetime.now()
print(f'todays date is: {akhon:%d/%m/%y}')
print(f'todays date is: {akhon:%d.%m.%y----%H:%M:%S}') #whatever i want
print(f"{akhon:%c}")
ic(f"{akhon:%I%p}") # 12 hours format
# -----------------------------------

x= 1.22123123123
print(x)
print(round(x,3))
print(f"four decimal places : {x:.4f}")
print(f"making it integer: {x:.0f}")
# --------------------


