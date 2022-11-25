import faker
import time

faker = faker.Faker()

i=0
while i<5:
    i+=1
    rand_date = faker.date_between('-400y','+200y')
    date_str = rand_date.strftime('%B %d, %Y')
    weekday_str = rand_date.strftime('%A')

    ans = input(date_str)
    if ans.lower()==weekday_str.lower():
        print('\n\N{check mark}\N{check mark}\N{check mark}\N{check mark}\N{check mark}\N{check mark}\N{check mark}\N{check mark} Correct! \N{check mark}\N{check mark}\N{check mark}\N{check mark}\N{check mark}\N{check mark}\N{check mark}\N{check mark}')
        time.sleep(1)
    else:
        print('\nXxXxXxXx Inorrect xXxXxXxX')
        time.sleep(1)

