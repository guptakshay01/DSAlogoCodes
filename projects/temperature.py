#   THIS FILE IS CREATED BY AKSHAY GUPTA
#   Calculate Avg temp and find temp above avg temp

num_days = int(input("Enter number of days for avg temp: "))

all_temp = []
total_temp = 0
for i in range(1, num_days+1):
    all_temp.append(int(input("Enter day "+ str(i) +" temp - ")))
    total_temp += all_temp[i]

avg_temp = round(total_temp/num_days, 2)
print('Avg temperature is', avg_temp)

count = 0
for i in range(num_days):
    if all_temp[i] > avg_temp:
        count += 1

print(count, "days have greater temp than avg.")