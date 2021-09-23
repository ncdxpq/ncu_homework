from question1.solution1_solo import leftup_solution,leftdown_solution,rightup_solution,rightdown_solution
from question1.answer import final_solution
import copy
# import time
def copyleftup(fuzhi, receive1):
    receive=copy.deepcopy(receive1)
    # 左上的数独赋值给中间
    for i in range(3):
        for j in range(3):
            receive[i][j] = fuzhi[i+6][j+6]
    return receive
def copyrightup(fuzhi, receive1):
    receive = copy.deepcopy(receive1)
    # 右上的数独赋值给中间数独
    for i in range(3):
        for j in range(3):
            receive[i][j+6] = fuzhi[i+6][j]
    return receive
def copyleftdown(fuzhi, receive1):
    receive = copy.deepcopy(receive1)
    # 左下的数独赋值给中间数独
    for i in range(3):
        for j in range(3):
            receive[i+6][j] = fuzhi[i][j+6]
    return receive
def copyrightdown(fuzhi, receive1):
    receive = copy.deepcopy(receive1)
    # 右下的数独赋值给中间数独
    for i in range(3):
        for j in range(3):
            receive[i+6][j+6] = fuzhi[i][j]
    return receive
# 检查99宫格第col列数字wantnum出现次数，若出现了两次(本数字也被记录了一次)，直接返回False
def judge_col(alist, col, wantnum):
    showtime = 0
    for times in range(9):
        if (alist[times][col] == wantnum):
            showtime += 1
        if showtime == 2:  # 最多才到2
            return False
    return True
# 检查99宫格row行数第字wantnum出现次数，若出现了两次(本数字也被记录了一次)，直接返回False
def judge_row(alist, row, wantnum):
    showtime = 0
    for times in range(9):
        if (alist[row][times] == wantnum):
            showtime += 1
        if showtime==2:  # 最多才到2
            return False
    return True
def judgeleftup(list99):
    for i in range(3):
        for j in range(3):
            if not(judge_col(list99,j,list99[i][j])):
                return False
            if not(judge_row(list99,i,list99[i][j])):
                return False
    return True
def judgerightup(list99):
    for i in range(3):
        for j in range(3):
            if not (judge_col(list99, j+6, list99[i][j+6])):
                return False
            if not (judge_row(list99, i, list99[i][j+6])):
                return False
    return True
def judgeleftdown(list99):
    for i in range(3):
        for j in range(3):
            if not (judge_col(list99, j, list99[i+6][j])):
                return False
            if not (judge_row(list99, i+6, list99[i+6][j])):
                return False
    return True
def judgerightdown(list99):
    for i in range(3):
        for j in range(3):
            if not (judge_col(list99, j+6, list99[i+6][j+6])):
                return False
            if not (judge_row(list99, i+6, list99[i+6][j+6])):
                return False
    return True
lenleftup=len(leftup_solution)
lenrightup=len(rightup_solution)
lenleftdown=len(leftdown_solution)
lenrightdown=len(rightdown_solution)
# 求解满足条件四个角的程序，之后再代入求单独数独解即可
mid_ori = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 9, 0, 0, 0, 0],
           [0, 0, 6, 0, 0, 0, 9, 0, 0],
           [0, 0, 0, 4, 0, 7, 0, 0, 0],
           [0, 1, 0, 0, 0, 0, 0, 8, 0],
           [0, 0, 0, 3, 0, 6, 0, 0, 0],
           [0, 0, 7, 0, 0, 0, 4, 0, 0],
           [0, 0, 0, 0, 5, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0]]
def main():
    print('开始解题\n')
    # time1=time.time()
    for i in range(lenleftup):
        # print("cost time:",time.time()-time1)
        temp1 = copyleftup(leftup_solution[i], mid_ori)
        # for ii in leftup_solution[i]:
        #     print(ii)
        # for ii in temp1:
        #     print(ii)
        if not (judgeleftup(temp1)):
            continue
        for j in range(lenrightup):
            # print('temp2')
            temp2 = copyrightup(rightup_solution[j], temp1)
            if not (judgerightup(temp2)):
                continue
            for k in range(lenleftdown):
                # print('temp3')
                temp3 = copyleftdown(leftdown_solution[k], temp2)
                if not (judgeleftdown(temp3)):
                    continue
                for m in range(lenrightdown):
                    # print('temp4')
                    temp4 = copyrightdown(rightdown_solution[m], temp3)
                    if not (judgerightdown(temp4)):
                        continue
                    if (final_solution(temp4) is True):  # 四边已经代入，求解最终数独
                        print('左上角的数独是:\n',leftup_solution[i])
                        print('右上角的数独是:\n', rightup_solution[j])
                        print('左下角的数独是:\n', leftdown_solution[k])
                        print('右下角的数独是:\n', rightdown_solution[m])
if __name__ == '__main__':
    main()

