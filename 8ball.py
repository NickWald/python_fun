import random

name = "nick"
question = "am I a good coder?\n"
ans = ""

random_num = random.randint(1, 9)
#print(random_num)

#control flow:
if random_num == 1:
  ans = "yes - definitely"
elif random_num == 2:
  ans = "it is decidedly so"
elif random_num == 3:
  ans = "without a doubt."
elif random_num == 4:
  ans = "reply hazy, try again."
elif random_num == 5:
  ans = "ask again later."
elif random_num == 6:
  ans = "better not tell you now."
elif random_num == 7:
  ans = "my sources say no."
elif random_num == 8:
  ans = "outlook not so good."
elif random_num == 9:
  ans = "very doubtful."
else:
  ans = "Error"

print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + ans)
