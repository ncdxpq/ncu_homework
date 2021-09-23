import copy
from question1.question import *


# 生成全为0的九宫格并返回
def new_list99():
    newlist = [[0 for i in range(9)] for j in range(9)]
    return newlist


# 打印99九宫格
def print_list99(list99):
    for rowx in range(9):
        if rowx != 0 and rowx % 3 == 0:
            print("- - - - - - - - - - -")
        for eachy in range(9):
            if eachy != 0 and eachy % 3 == 0:
                print("|", end=' ')
            print(list99[rowx][eachy], end=' ')
        print(" ")


# 修改九宫格第x行，y列为z
def z_to_listxy(x, y, z, list99):
    list99[x][y] = z
    return list99


# 检查99宫格第col列数字wantnum出现次数，返回int
def show_nums_in_col(alist, col, wantnum):
    showtime = 0
    for times in range(9):
        if (alist[times][col] == wantnum):
            showtime += 1
    return showtime


# 检查99宫格第row行数字wantnum出现次数，返回int
def show_nums_in_row(alist, row, wantnum):
    showtime = 0
    for times in range(9):
        if (alist[row][times] == wantnum):
            showtime += 1
    return showtime


# 检查99宫格第squarenum块数字wantnum出现次数,x范围：(1,2,3)。y范围：(1,2,3)
def show_nums_in_square(alist, squarenumy, squarenumx, wantnum):
    showtime = 0
    for i in range(squarenumy * 3 - 3, squarenumy * 3):  # 0-3，3-6，6-9
        for j in range(squarenumx * 3 - 3, squarenumx * 3):
            if (alist[i][j] == wantnum):
                showtime += 1
    return showtime


# 检查99宫格第col列的wantnum的出现位置，返回位置的二维列表
def show_post_in_col(alist, col, wantnum):
    showpost = []
    for times in range(9):
        if (alist[times][col] == wantnum):
            showpost.append([times, col])
    return showpost


# 检查99宫格第row行的wantnum的出现位置，返回位置的二维列表
def show_post_in_row(alist, row, wantnum):
    showpost = []
    for times in range(9):
        if (alist[row][times] == wantnum):
            showpost.append([row, times])
    return showpost


# 检查99宫格第yx块的wantnum的出现位置，返回位置的二维列表
def show_post_in_square(alist, squarenumy, squarenumx, wantnum):
    showpost = []
    for i in range(squarenumy * 3 - 3, squarenumy * 3):
        for j in range(squarenumx * 3 - 3, squarenumx * 3):
            if (alist[i][j] == wantnum):
                showpost.append([i, j])
    return showpost


# 判断是否已全部解完，返回boolean
def whetherfinal(list99):
    for i in range(9):
        for j in range(9):
            if (list99[i][j] == 0):  # 还有0，没解完
                return False
    return True  # 解完了


# 以是否有最少方法的数字完成解来判断是否往下有解
def whether_have_solution(list99):
    num, num_pro, num_post = show_least_can_num(list99)
    # 没有可以放的地方且数独没有解完
    if (num == 0 and not whetherfinal(list99)):
        return False
    return True


def where_cannot_put(temp, list99):
    # 新建一个空白的9*9列表
    list_already_exit = new_list99()
    for i in range(9):
        for j in range(9):
            if (show_nums_in_row(list99, i, temp) != 0 or
                    show_nums_in_col(list99, j, temp) != 0 or
                    list99[i][j] != 0):
                list_already_exit[i][j] = 1
    for i in range(1, 4):
        for j in range(1, 4):
            if (show_nums_in_square(list99, i, j, temp) != 0):
                for x in range(i * 3 - 3, i * 3):
                    for y in range(j * 3 - 3, j * 3):
                        list_already_exit[x][y] = 1
    return list_already_exit


# 显示可确定放置的数字,返回该数字
def show_only_one_can_num(list99):
    for nums in range(1, 10):
        listpro = where_cannot_put(nums, list99)
        # 唯一确定
        for y in range(9):
            if (show_nums_in_col(listpro, y, 0) == 1 or show_nums_in_row(listpro, y, 0) == 1):  # 只有一个空可填入
                return nums
        for i in range(1, 4):
            for j in range(1, 4):
                if (show_nums_in_square(listpro, i, j, 0) == 1):
                    return nums
    return 0

# 在 某个数 的可能性表中的某行/列/块show_mostpro_exa_num中有最少的0
# 寻找可放置块的所有方法最少的数字，返回该数字和最少方法的方法数和地方
# type 1按列 2按行 3按块 post 绝对坐标的列表的列表
def show_least_can_num(list99):
    # 如果this_num为0，代表数独已解完或数独遇到了死解，这个将会在后面解决多种解法的数独中用到
    this_num = 0  # 这个数this_num
    this_num_num = 9  # 最少有this_num_num 个零，9为初始值
    this_num_position = []  # 将会以二维列表的形式返回数字0在该i行/列/块的绝对坐标（[行，列], [行，列]…）
    for anum in range(1, 10):
        prolist = where_cannot_put(anum, list99)  # 分别获得数字1-9的可能性表，进行对比
        for i in range(9):
            # 可能性表在列中的最小0值
            if (show_nums_in_col(prolist, i, 0) != 0 and show_nums_in_col(prolist, i, 0) < this_num_num):
                this_num_num = show_nums_in_col(prolist, i, 0)  # 最少0值的有多少0
                this_num = anum  # 记录可能性表中拥有最少0值的数字
                this_num_position = show_post_in_col(prolist, i, 0)  # 二维列表坐标[]（[行，列], [行，列]…）
            # 可能性表在行中的最小0值
            if (show_nums_in_row(prolist, i, 0) != 0 and show_nums_in_row(prolist, i, 0) < this_num_num):
                this_num_num = show_nums_in_row(prolist, i, 0)
                this_num = anum
                this_num_position = show_post_in_row(prolist, i, 0)
        for sy in range(1, 4):
            for sx in range(1, 4):
                # 该块中有0，且该块中的0的数量更少
                if (show_nums_in_square(prolist, sy, sx, 0) != 0 and show_nums_in_square(prolist, sy, sx,
                                                                                         0) < this_num_num):
                    this_num_num = show_nums_in_square(prolist, sy, sx, anum)
                    this_num = anum
                    this_num_position = show_post_in_square(prolist, sy, sx, 0)
    # 1-9可能性表中拥有最少0值的数字，最少有this_num_num 个零，二维列表坐标
    return this_num, this_num_num, this_num_position


# 确切放置数字直到无确切数字,返回新9*9
def solution_until_have_more_action(list99):
    while (True):
        this_num, this_num_num, this_num_position = show_least_can_num(list99)
        if (this_num_num != 1):
            return list99
        else:
            list99[this_num_position[0][0]][this_num_position[0][1]] = this_num


# 根据已知最小可能的数字及其位置来递归讨论并更改多种可能的情况
# 保证传入的数独已按照一种解法的解完！！！savelist非常重要，保证尝试失败后能够原样恢复尝试前的数独
def final_solution(listtemp):
    savelist = copy.deepcopy(listtemp)
    partial_solve_list = solution_until_have_more_action(copy.deepcopy(listtemp))
    if (not whether_have_solution(partial_solve_list)):
        return False
    if (whetherfinal(partial_solve_list)):
        global current_shudu
        current_shudu = copy.deepcopy(partial_solve_list)
        print("*********求出一种解法**********\n")
        global solution_number
        # solution_number += 1
        # global k
        # print(k)
        # if k == 0:
        #     leftup_solution.append(current_shudu)
        # elif k == 1:
        #     leftdown_solution.append(current_shudu)
        # elif k == 2:
        #     rightup_solution.append(current_shudu)
        # else:
        #     rightdown_solution.append(current_shudu)
        print('中间的数独是：\n',current_shudu)  # 原数据输出
        # print_list99(current_shudu)  # 带边框输出
        return True
    # 单一解后，数独还没塞满
    # 列出当前最优数独的相关参数,递归部分
    cur_num, cur_num_num, cur_num_post = show_least_can_num(partial_solve_list)
    if (cur_num == 0):  # 应该不会出现这种情况
        return False
    for each_post in cur_num_post:  # 遍历每个可以放置的位置,将数字放入进行验证
        change_list = z_to_listxy(each_post[0], each_post[1], cur_num, copy.deepcopy(partial_solve_list))

        if (final_solution(change_list)):  # 根据尝试的填入一个数字如果能解通就返回true
                partial_solve_list = copy.deepcopy(savelist)  # 求多解，还原这次猜测，再次猜
                continue
        else:  # 没有解出来，还原
            partial_solve_list = copy.deepcopy(savelist)  # 如果根据尝试填入的解不通就还原数独。继续for循环

    return False


# -----------------------------------------------
if __name__ == '__main__':

    # leftup_solution = []
    # leftdown_solution = []
    # rightup_solution = []
    # rightdown_solution = []
    # questiondict = {0: leftup_ori, 1: leftdown_ori, 2: rightup_ori, 3: rightdown_ori, 4: mid_ori}
    # solvenum = [0, 0, 0, 0, 0]
    # for i in range(4):  # range(5)时同时算出mid_solo的解
    #     global k
        # k = i
        # current_shudu = questiondict[i]  # 第一个数独开始解
    solution_number = 0
    final_solution(current_shudu)
    #     solvenum[i] = solution_number
    # for i in range(4):
    #     print('单独的数独{}\n拥有{}种解法'.format(questiondict[i], solvenum[i]))
    # f = open("./solution1_solo.py", 'a')
    # f.write('leftup_solution='+str(leftup_solution)+'\n')
    # f.write('leftdown_solution='+str(leftdown_solution)+'\n')
    # f.write('rightup_solution='+str(rightup_solution)+'\n')
    # f.write('rightdown_solution='+str(rightdown_solution)+'\n')
