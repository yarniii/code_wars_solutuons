def square_digits(num):
    # Your code here
    num=str(num)
    sum=0
    concet=''
    for i in num:
        sum+=int(i)**2
        concet+=str(int(i)**2)
        
    return int(concet)
