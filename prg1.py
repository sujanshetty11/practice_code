import csv 
step =0
td=[]

with open("ENJOYSPORT.csv", newline='') as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        td.append(row)

hypo=['0']*(len(td[0])-1)

for ex in td:
    if ex[-1]=='1':
        for i in range(len(hypo)):
            if hypo[i]!=ex[i]:
                if hypo[i]=='0':
                    hypo[i]=ex[i]

                else:
                    hypo[i]='?'
    print(f"step {step} :")
    print(hypo)
    step+=1
    print("\n")
print(hypo)
