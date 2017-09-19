#this is just the beginning of something big


print ('strating')

day = 0
flag = 0
comp_money = [10000]
salary = 10
happiness = 0
quality = 1
def worker_happiness(salary):
    happiness = salary /9
    return happiness

def costumer(happy):
    # if happy > 8:
    #    pay = 8*2.5
    # else:
    #     pay = happy*2.5

    pay= ((happy/10)-0.05)*100

    return pay

def product(worker_happiness):
    quality = worker_happiness
    return quality




for day in range(0,100):
    flag = flag + 1

    if comp_money[-1] <= 0:
        print("No more money!")
        break

    # if (comp_money - salary )> 0:
    if day > 10:

        num_da_media = []
        media = 0
        for i in range(1,10):


            num_da_media.append(comp_money[-i] - comp_money[-i-1])
            # print(num_da_media[-1])

        media = sum(num_da_media)/len(num_da_media)
        print(media)
        # if media < 0:
        #     salary += 1

        if flag >= 5:
            if media < 0:
                salary += 5
            flag = 0

    # try:
    #     print(media)
    # except:
    #     print ('ops')

    comp_money_temp = comp_money[-1]
    comp_money_temp -= salary
    comp_money_temp += costumer(quality)



    happiness = worker_happiness(salary)
    quality = product(happiness)

    comp_money.append(comp_money_temp)

    # print(comp_money[-1])

