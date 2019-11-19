def convo():
    print("Hello User!")
    name = input("What is your name? ")
    print(f"Hello {name}")
    age = int(input("What is your age? "))
    if age < 18:
        print ("Awwww. you're just a baby")
    elif age > 18:
        print("Ah... A well traveled soul are ye!")

candies = ['[0] Snickers', '[1] Kit-Kat', '[2] Sour Patch Kids', '[3] Juicy Fruit', '[4] Swedish Fish', '[5] Skittles', '[6] Starbursts', '[7] M&Ms']
print(candies)
takeHome = []
i = 0
for i in range(5):
    candy = int(input('Pick a candy'))
    takeHome.append(candy)

print(takeHome)