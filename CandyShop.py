candyList = [
    'Snickers',
    'Skittles',
    'Twix',
    'Hershey Bar',
    'Starbursts',
    'Juicy Fruit',
    'Junior Mint'
]

allowance = 5
candyCart = []

print("you can pick 5 candies")
print("which candy do you wanna bring home? ")
for x in range(allowance):
    selected = input("Input the index of candy you want: ")

    candyCart.append(candyList[int(selected)])

print('I brought home with me...')
for candy in candyCart:
    print(candy)