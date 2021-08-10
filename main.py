# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3] #Nested list
print(f"{row1}\n{row2}\n{row3}") #New line added
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#23
#Write your code below this row 👇
#map = str[row1, row2, row3]
#position == str

column_v=int(position[0]) #2
row_h = int(position[1]) #3

#print(map[0])
#print(map[1])

#Create a new list where we look for the row
#select_row = map[row_h -1]
#print(type(select_row))

# within that row, we look for the column
#select_row[column_v -1] = "X"

#Resolving by first looking for either row or column as a list and then column as an item within that row
map[row_h - 1][column_v - 1] = "X"


#print(map[row_h -1]) #Remember that the its the list within nested list "map"
#selected_row = map[row -1]
#selected_row[horizontal - 1] =

#print(type(position))

#print(type(map))
#column1 = [row1[0], row2[0], row3[0]]
#print(column1)
#column2 = [row1[1], row2[1], row3[1]]
#print(column2)
#column3 = [row1[2], row2[2], row3[2]]
#print(column3)

#map2 = [column1, column2, column3]
#map2 = str[column1, column2, column3]
#print(type(map2))

#count1 = len(row1)
#count2 = len(row2)
#count3 = len(row3)
#count4 = len(column1)
#count5 = len(column2)
#count6 = len(column3)

#print(count1)

#position = ["map[0][0]", "map2[0][0]"]

#comma_remove = position.split(",")

#print(comma_remove)
#print(position)
#names = names_string.split(", ")

#first_digit == column1[0,count4 -1], column2[0,count5 -1], column3[0,count6 -1]
#first_digit == column1 or column2 or column3
#second_digit = row1, 


#print(row2[2])

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
