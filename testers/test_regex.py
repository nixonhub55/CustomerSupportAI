import re

q = "who is the customer has phone number 0922233311?"

print(q)

patterns = [
    r"09\d{8}",
    r"09\d{9}",
    r"\d+",
    r"0922233311"
]

for p in patterns:
    m = re.search(p, q)
    print(f"{p} ->", m.group() if m else None)