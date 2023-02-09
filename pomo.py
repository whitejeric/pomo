from time import sleep
from tqdm import tqdm
import os
work = 1800 #30 minutes
play = 300 #5 minutes
while(True):
    print('Working')
    for i in tqdm(range(work)):
        sleep(1)
    os.system('cls')
    print('Playing')
    for i in tqdm(range(play)):
        sleep(1)
    os.system('cls')
