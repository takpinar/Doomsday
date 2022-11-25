import faker
import time
import random
from termcolor import colored

faker = faker.Faker()
num_qs = random.randrange(5,10)
i=0
sum_time = 0
score = 0

while i<num_qs:
    i+=1
    rand_date = faker.date_between('-400y','+200y')
    date_str = rand_date.strftime('%B %d, %Y')
    weekday_str = rand_date.strftime('%A')
    question = date_str + ' ?\n'

    start = time.time()
    print('*-.-*-.-*-.-*-.-*-.-*-.-*-.-*-.-*')
    ans = input(question)
    dur = time.time() - start
    sum_time += dur

    if ans.lower()==weekday_str.lower():
        score += 1
        print(colored('\N{check mark}','green'))
        time.sleep(1)
    else:
        print(colored('X','red'))
        time.sleep(1)

perc = round(score/num_qs,2)
avg_time = round(sum_time/num_qs,2)
print('\n---------------------------------------')
print("Accuracy: ",perc, '%')
print("Average Time: ", avg_time,'sec.')
print('---------------------------------------')
