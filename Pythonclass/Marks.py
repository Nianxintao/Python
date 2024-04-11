 # if marks is>80 -> D
 # if marks 60-80 -> first d


marks = int(input("what is your mark: "))
if(marks >= 80 ):
    print("D")
elif (marks>= 60 and marks <80):
    print("first d")
elif (marks >=50 and marks <60):
    print("c")
elif (marks<50):
    print("fail")