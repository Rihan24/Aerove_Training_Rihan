def is_prime(n):
    if n==1:
        return False
    for j in range(2,round((n**0.5))+1):
        if n%j==0:
            return False
    return True


a=int(input())
lst=[]
wfile=open("myFirstFile.txt","w")
for i in range((10**(a-1)),(10**a)-3):
    if (is_prime(i)==True) and (is_prime(i+2)==True):
        wfile.write(str(i)+" "+ str(i+2))
        wfile.write("\n")
wfile.close()





