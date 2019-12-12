#def is_even(a):
#    if a % 2 == 0:
#        return True
#    else: 
#        return False

#print (is_even(420))

def evens(a):
    res = []
    for n in a: 
        if n % 2 == 0:
            res.append(n)
    return res

a = [420, 840, 0.643 ,12, 6563, 35, 325]

print (evens(a))