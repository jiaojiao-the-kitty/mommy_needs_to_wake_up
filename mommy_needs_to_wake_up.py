import random
import time

def pawing_door():
    print("thump!")

door_closed=True
meow_list=["mmmmmeow","meoooow","prrrrr meow","meeeeeeeeeow"]
meow_count=0
meow=random.choice(meow_list)

while door_closed:
    print(meow)
    meow_count +=1
    if meow_count % 6 == 5:
        time.sleep(120)
        meow=random.choice(meow_list)
        pawing_door()
