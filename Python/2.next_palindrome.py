def check_palindrome(n):
    string=str(n)
    if string[::]==string[::-1]:
        return True
    else:
        return False
a=int(input())

while True:
    if check_palindrome(a+1)==True:
        print(a+1)
        break

    a=a+1