# 读取本地txt
def read_txt():
    with open('init copy.txt', 'r') as f:
        return f.read()
    
chess= read_txt()
print(chess)

# 按照换行符分割
chess_line = chess.split('\n')
# print(chess_line[1])

def pick(chess,order_choose,order_arrive):
    # order_dict={"一":1,"二":2,"三":3,"四":4,"五":5,"六":6,"七":7,"八":8,"九":9}
    chess_board=chess.split('\n')
    chess_line=[]
    for i in range(len(chess_board)):
        chess_line.append(chess_board[i].split(','))
    chess_line=chess_line[1:]
    order_choose=order_choose.split(',')

    tmp_col=int(order_choose[1])
    tmp_row=int(order_choose[0])
    if "[" in chess_line[tmp_row-1][tmp_col-1]:
        tmp=' '+chess_line[tmp_row-1][tmp_col-1][2:]
        a=chess_line[tmp_row-1][tmp_col-1][:2]
        chess_line[tmp_row-1][tmp_col-1]=f"{a}'---'"
    elif "]" in chess_line[tmp_row-1][tmp_col-1]:
        tmp=chess_line[tmp_row-1][tmp_col-1][:-1]
        chess_line[tmp_row-1][tmp_col-1]=" '---']"
    else:
        tmp=chess_line[tmp_row-1][tmp_col-1]
        chess_line[tmp_row-1][tmp_col-1]=" '---'"
        
    order_arrive=order_arrive.split(',')

    tmp_col=int(order_arrive[1])
    tmp_row=int(order_arrive[0])
    
    if "[" in chess_line[tmp_row-1][tmp_col-1]:
        a=chess_line[tmp_row-1][tmp_col-1][:2]
        tmp=tmp[1:]
        chess_line[tmp_row-1][tmp_col-1]=f"{a}{tmp}"
    elif "]" in chess_line[tmp_row-1][tmp_col-1]:
        chess_line[tmp_row-1][tmp_col-1]=f"{tmp}]"
    else:
        chess_line[tmp_row-1][tmp_col-1]=f"{tmp}"
    
    return chess_line

# # 从键盘输入
print("按照'1,1'的格式输入")
order_choose = input("选择要动的棋子：")
order_arrive = input("选择要到达的位置：")
# order_choose = '一,1'
# order_arrive = '三,1'
chess_line=pick(chess,order_choose,order_arrive)
# print(chess_line)
# 合并chess_line

result_str = '\n'.join([','.join(sublist) for sublist in chess_line])
a="零[' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ']"
result_str=a+'\n'+result_str
print(result_str)
with open("init copy.txt", "w") as file:
    file.write(result_str)