import faker
import time
import random
from termcolor import colored

faker = faker.Faker()
num_qs   = 5
i        = 0
sum_time = 0
score    = 0
colors   = ['red','yellow','cyan','green']

hi_score_path = "/home/takpinar/desktop/Doomsday/hi_score.txt"
file = open(hi_score_path,"r")
hisc = float(file.read()[8:-1])
file.close()
himins = round(hisc//60,1)
hisecs = round(hisc%60,1)

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
    
    if ans == 'q':
        print('quit')
        quit()
    elif ans.lower()==weekday_str.lower():
        score += 1
        print(colored('\N{check mark}','green'))
        time.sleep(.1)
    else:
        print(colored('X','red'))
        time.sleep(.1)     
    
perc = round(score/num_qs,2)*100
best = False

if (perc == 100.0 and hisc > sum_time) or hisc == '':
    print('BEST')
    file = open(hi_score_path,"w")
    file.write("hiscore=" + str(round(sum_time,2)))
    file.close()
    himins = round(sum_time//60,1)
    hisecs = round(sum_time%60,1)
    best = True

mins = round(sum_time//60,0)
secs = round(sum_time%60,0)
avg_time = round(sum_time/num_qs,2)

print('---------------------------------------')
print(colored("Accuracy:     {} %".format(perc),colors[int((score/num_qs)//0.3)]))
if best:
    print(colored("New Best Time:   {} min. {} sec.".format(mins, secs),'green'))
else:
    print("Total Time:   {} min. {} sec.".format(mins, secs))
print("Average Time: {} sec.".format(avg_time))
print('---------------------------------------')
print("High Score:   {} min. {} sec.".format(himins, hisecs))
print('---------------------------------------')
