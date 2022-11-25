import faker
import time
import random
from termcolor import colored

faker = faker.Faker()
# num_qs = random.randrange(5,10)
num_qs = 7
i=0
sum_time = 0
score = 0
begin = time.time()

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
        # time.sleep(1)
    else:
        print(colored('X','red'))
        # time.sleep(1)
        
tot_time = time.time() - begin
mins = round(tot_time//60,0)
secs = round(tot_time%60,0)
perc = round(score/num_qs,2)
avg_time = round(sum_time/num_qs,2)

print('---------------------------------------')
print("Accuracy:     {} %".format(perc))
print("Total Time:   {} min. {} sec.".format(mins, secs))
print("Average Time: {} sec.".format(avg_time))
print('---------------------------------------')
