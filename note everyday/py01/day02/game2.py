import random

all_choices = ['石头', '剪刀', '布']
# 人在前，计算机在后，组成小列表，把人赢的情况再放到大列表中
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
computer = random.choice(all_choices)
player = input('请出拳(石头/剪刀/布): ')

print("Your choice: %s, computer's choice: %s" % (player, computer))
if player == computer:
    print('平局')
elif [player, computer] in win_list:
    print('You WIN!!!')
else:
    print('You LOSE!!!')
