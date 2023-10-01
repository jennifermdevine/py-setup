def hello():
    print("Hello!")

def pack(item_one, item_two, item_three):
    return [item_one, item_two, item_three]

def eat_lunch(lunch_items):
    if len(lunch_items) == 0:
        print("My lunchbox is empty")
    else:
        for index in range(len(lunch_items)):
            if index == 0:
                print(f"First I eat {lunch_items[index]}")
            else:
                print(f"Then I eat {lunch_items[index]}")

hello()
print (pack("cheese", "bacon", "toast"))
eat_lunch(pack("toast", "bacon", "cheese"))