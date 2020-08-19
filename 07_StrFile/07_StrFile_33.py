file_1, file_2 = input().strip().split()

op_1 = open(file_1, 'r')
op_2 = open(file_2, 'r')

line_1 = op_1.readline().strip()
line_2 = op_2.readline().strip()


while line_1 and line_2:
    idx_1, score_1 = line_1.split()
    idx_1 = int(idx_1)

    idx_2, score_2 = line_2.split()
    idx_2 = int(idx_2)

    if idx_1 % 100 > idx_2 % 100:
        print(idx_2, score_2)
        line_2 = op_2.readline().strip()
    elif idx_1 % 100 < idx_2 % 100:
        print(idx_1, score_1)
        line_1 = op_1.readline().strip()
    else:
        if idx_1 > idx_2:
            print(idx_2, score_2)
            line_2 = op_2.readline().strip()
        else:
            print(idx_1, score_1)
            line_1 = op_1.readline().strip()

while line_1:
    idx_1, score_1 = line_1.strip().split()
    print(idx_1, score_1)
    line_1 = op_1.readline().strip()

while line_2:
    idx_2, score_2 = line_2.strip().split()
    print(idx_2, score_2)
    line_2 = op_2.readline().strip()
