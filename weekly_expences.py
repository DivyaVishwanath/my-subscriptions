import itertools

def Expenses(inp):
# Mapping weekly cost with name in a dictionary
    Dic = {
    26:"TOI",
    20.5:"Hindu",
    34: "ET",
    10.5:"BM",
    18:"HT",
    };
    var=[26,20.5,34,10.5,18]
    newp=[]
# storing all possible combinations to a variable
    join=list(itertools.combinations(var, 2))
    for i in join:
        if sum(i)<=inp: #Fitering  combinations based on the weekly budget
            newp.append(i)
    
    np=[]
    for i in range(len(newp)):
        var1=newp[i][0]
        var2=newp[i][1]
        np.append((Dic[var1],Dic[var2])) # Getting values for keys
    print(np)


inp=int(input())
Expenses(inp)