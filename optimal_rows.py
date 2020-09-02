import itertools

def find_sum(rows, matrix):
    all_squares =[]

    #get list of all squares in the 3 lines
    for r in rows:
        if r >= 0 and r <= 4:
            all_squares = all_squares + matrix[r]
        elif r >= 5 and r <= 9:
            r = r-5
            all_squares = all_squares + [matrix[i][r] for i in range(5)]
        else:
            #TLBR
            if r == 10:
                all_squares = all_squares + [matrix[i][i] for i in range(5)]
            else:
                all_squares = all_squares + [matrix[i][4-i] for i in range(5)]
    
    #remove duplicates
    res = []
    for i in all_squares:
        if i not in res:
            res.append(i)
    return sum(res)

def main():
    file1 = open("matrix.txt")
    lines = file1.readlines()
    matrix = []
    row_ints=[]
    for line in lines:
        row = line.split(" ")
        if(len(row) != 5):
            print("matrix must be 5x5")
            return
        row[4] = row[4].replace("\r\n", "")
        row_ints = list(map(int,row))
        matrix.append(row_ints)
    if(len(matrix) !=5):
        print("matrix must be 5x5")
        return
    file1.close()
    #rows: 0-4, cols:5-9, diags=10,11
    idx_list = [i for i in range(12)]

    #iterate all combinations of lines
    combinations= list(itertools.combinations(idx_list,3))
    sum_list = []
    for comb in combinations:
        #find sum of 3 lines, append with sum and combination tuple
        sum_list.append([find_sum(comb, matrix),comb])
    sum_list.sort()
    #get top 5 sums
    top_5 = sum_list[:5]

    print("Best Routes")
    for route in top_5:
        print("Total Sum: " + str(route[0]))
        for r in route[1]:
            if r >= 0 and r <= 4:
                print("Row "+str(r+1))
            elif r >= 5 and r <= 9:
                r = r-5
                print("Col "+str(r+1))
            else:
                #TLBR
                if r == 10:
                    print("Diag TLBR")
                else:
                    print("Diag BLTR")
        print("---------------------------------------")
    

if __name__=="__main__":
    main()