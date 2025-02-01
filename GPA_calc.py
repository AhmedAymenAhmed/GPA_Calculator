#GPA calc #/4
count=0
sum=0
hours=0
fail=0
f=float
i=input
p=print
num_flag="yes"
while num_flag=="yes":
    try:
        sub_num=int(i("How many subjects you have? "))
        if sub_num>0:
            num_flag="no"
        else:
            num_flag="yes"
    except ValueError:
        p("Entar a number please ")
        flag="yes"
num=f(sub_num)
hours_flag="yes"
while (num>count):
    grade=i(f"Enter your grade in subject{count+1} ").upper()
    while hours_flag=="yes":
        try:
            hours_count=f(i("how many hours?" ))
            if hours_count>0:
                hours_flag="no"
            else:
                p("Invalid input")
                hours_flag="yes"
        except ValueError:
            p("Enter a number please")
            hours_flag="yes"
    hours_flag="yes"
    if grade=="A":
        sum=sum+4.000*hours_count
    elif grade=="A-":
        sum=sum+3.666*hours_count
    elif grade=="B+":
        sum=sum+3.333*hours_count
    elif grade=="B":
        sum=sum+3.000*hours_count
    elif grade=="B-":
        sum=sum+2.666*hours_count
    elif grade=="C+":
        sum=sum+2.333*hours_count
    elif grade=="C":
        sum=sum+2.000*hours_count
    elif grade=="C-":
        sum=sum+1.666*hours_count
    elif grade=="D+":
        sum=sum+1.333*hours_count
    elif grade=="D":
        sum=sum+1.000*hours_count
    elif grade=="F":
        sum=sum
        fail=fail+1
    else :
        p("Invalid grade")
        count=count-1
    count=count+1
    hours=hours+hours_count
    flag="no"
gpa=sum/hours
p(f"Your gpa is {gpa}")
if fail==0:
    p("You didn't fail any subject")
elif fail==1:
    p("You failed 1 subject")
else :
    p(f"you failed {fail} subjects")