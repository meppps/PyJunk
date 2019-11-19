name = "Gerald"
group_one = ["Greg", "Tony", "Susan"]
group_two = ["Gerald", "Paul", "Ryder"]
group_three = ["Carla", "Dan", "Jefferson"]

if name in group_one:
    print(name + " is in the first group")
elif name in group_two:
    print(name + " is in group two")
elif name in group_three:
    print(name + " is in group three")
else:
    print(name + " does not have a group")

