import random

# num_list = random.sample(range(1, 6),no_times)
# print(num_list[1:],end="")
def roll(roll_time):
    rollnum=[]
    for i in range(0,roll_time):
        num=random.randint(1,6)
        rollnum.append(num)
    return  rollnum

def main():
    while True:
        try:
            no_times=input("how many time syou would like to roll the dice: ")
            if no_times=="exit":
                print("Thank you for coming!!")
                break
            roll(int(no_times))
        except:
            print("Please Enter the correct value: ")
