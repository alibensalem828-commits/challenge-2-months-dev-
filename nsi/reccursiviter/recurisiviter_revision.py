#exos 1
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else :
        return fibonacci(n-2)+fibonacci(n-1)

print(fibonacci(4))

#exos4 
'''def est_palindrome(texte):
    if len(texte)<=1:
        return True 
    elif texte[-1]!= texte[0]:
        return False
    else:
       return est_palidrome(texte[0:-1])
print(est_palindrome('AYA'))'''


print("="*15)