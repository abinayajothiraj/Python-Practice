#eg 1: while loop

i=1
while i<6:
    print(i)
    i=i+1


def is_valid_string(s):
    if len(s)>3 and s!="":
        return True
    else:
        return False
print(is_valid_string(""))

#doubt:
for x in ["red","big"]:
    for y in ["apple","banana"]:
        print(x,y)








