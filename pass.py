import random
lower = "netagovindk"
upper = "NETAGOVINDK"
number = "257"
symbol = "@$!*%&"

all = lower + upper + number + symbol
length = 9

password = "".join(random.sample(all, length))
print(password)