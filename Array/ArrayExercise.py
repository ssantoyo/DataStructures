Month = ["Jan", "Feb","Mar", "Apr", "May"]
Expense = [2200,2350,2600,2130,2190]


# 1. In Feb, how many dollars you spent extra compare to January?
print(Expense[1]-Expense[0])
# 2. Find out your total expense in first quarter (first three months) of the year.
print(sum(Expense[0:3]))
# 3. Find out if you spent exactly 2000 dollars in any month
for idx in range(len(Expense)):
    if Expense[idx] == 2000:
        print("Spent Exactly 2000 in the month of", Month[idx])
    else:
        print("Spent more than 2000 in ", Month[idx])
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
Month.append("Jun")
Expense.append(1980)
print(Expense)
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
Expense[3] = 1930
print(Expense)


#####################################################
heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
print(len(heros))
# 2. Add 'black panther' at the end of this list
heros.append("black panther")
print(heros)
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
heros.remove("black panther")
heros.insert(3,"black panther")
print(heros)

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.

#My Answer
heros = ["doctor strange" if hero == "thor" or hero == "hulk" else hero for hero in heros]
print(heros)
#instructors Answer
heros[1:3]=['doctor strange']
print(heros)
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros = sorted(heros)
print(heros)

######################################################
#Create a list of all odd numbers between 1 and a max number. 
# Max number is something you need to take from a user using input() function
def oddToMax(n):
    odds = []
    for i in range(n):
        if i%2 != 0:
            odds.append(i)
    return odds

print(oddToMax(100))