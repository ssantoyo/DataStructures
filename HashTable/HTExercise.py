'''
nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,

What was the average temperature in first week of Jan
What was the maximum temperature in first 10 days of Jan

Figure out data structure that is best for this problem
'''

# arr = []

# with open("nyc_weather.csv", "r") as file:
#     for line in file:
#         tokens = line.split(',')
#         try:
#             temp = int(tokens[1])
#             arr.append(temp)
#         except:
#             print("Invalid tempeture: Ignore this line")
    
#     print("Average Temp in first week: ", sum(arr[0:7])/len(arr[0:7]))
#     print("Max Temp: ", max(arr[0:10]))

'''
(2) nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,

  (a) What was the temperature on Jan 9?

  (b) What was the temperature on Jan 4?

  Figure out data structure that is best for this problem
'''

# arr = {}

# with open("nyc_weather.csv", "r") as f:
#     for line in f:
#         tokens = line.split(',')
#         try:
#             day = tokens[0]
#             temp = int(tokens[1])
#             arr[day] = temp
#         except:
#             print("Invalid tempeture or day: Ignore this line")
#     print("Jan 9 Temp: ", arr["Jan 9"])
#     print("Jan 4 Temp: ", arr["Jan 4"])

'''
poem.txt Contains famous poem "Road not taken" by poet Robert Frost. 
You have to read this file in python and print every word and its count as show below. 
Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.

 'diverged': 2,
 'in': 3,
 'I': 8
'''

wordCount = {}

with open("poem.txt", "r") as f:
    for line in f:
    #    print(line)
        tokens = line.split()
        for token in tokens:
            token = token.replace("\n","")
            if token in wordCount:
                wordCount[token] += 1
            else:
                wordCount[token] = 1
    print(wordCount)
    print('diverged: ', wordCount["diverged"])
    print('in: ', wordCount["in"])
    print('I: ', wordCount["I"])
           
    