items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("duplicate",item)
        break
    # break use to break the thing eg. the loop 
    unique_item.add(item)