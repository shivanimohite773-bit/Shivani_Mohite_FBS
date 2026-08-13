
amount = int(input("Enter amount: "))

n500 = amount // 500
amount = amount % 500

n200 = amount // 200
amount = amount % 200

n100 = amount // 100
amount = amount % 100

n50 = amount // 50
amount = amount % 50

n20 = amount // 20
amount = amount % 20

n10 = amount // 10
amount = amount % 10

print("500 Notes =", n500)
print("200 Notes =", n200)
print("100 Notes =", n100)
print("50 Notes =", n50)
print("20 Notes =", n20)
print("10 Notes =", n10)