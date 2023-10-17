def hello():
    print("Hello user welcome to Python")


hello()

greeting = []


def pack(str1, str2, str3):
    greeting.append(str1)
    greeting.append(str2)
    greeting.append(str3)
    return greeting


print(pack("How", "Are", "You"))


def eat_lunch(fooditems):
    if len(fooditems) == 0:
        print("My lunchbox is empty!")

    for item in fooditems:
        if item == "Sandwich":
            print("First i eat" + " " + item)
        elif item == "Cupcake":
            print("Next i eat" + " " + item)
        else:
            print("Finally i eat" + " " + item)


eat_lunch(["Sandwich", "Cupcake", "Fish"])
