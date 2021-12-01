def number_of_bottles():
    for i in range(99,-1,-1):
        if i == 0:
            print(f"No more bottles of milk on the wall, no more bottles of milk.\nGo to the store and buy some more, {i+99} bottles of milk on the wall.")
            break
        elif i == 1:
            print(f"{i} bottle of milk on the wall, {i} bottle of milk.\nTake one down and pass it around, no more bottles of milk on the wall.")
        elif i == 2:
            print(f"{i} bottles of milk on the wall, {i} bottles of milk.\nTake one down and pass it around, {i-1} bottle of milk on the wall.")
        else:
            print(f"{i} bottles of milk on the wall, {i} bottles of milk.\nTake one down and pass it around, {i-1} bottles of milk on the wall.")

number_of_bottles()