from math import sqrt, pi
def PiLeibniz(n):
    s = 0
    for i in range(n+1):
        s += 1/((4 * i + 1) * (4 * i + 3))
    s = s * 8
    return s
#print("PiLeibniz=" ,PiLeibniz(100))
def PiEuler(n):
    s = 0
    for i in range(1, n+1):
        s += 1/(i * i)
    s = sqrt(6 * s)
    return s
#print("PiEuler=", PiEuler(100))
def PiWallis(n):
    p=1
    for i in range(1,n+1):
        p*=(4*i**2)/(4*i**2-1)
    p = 2*p
#    p = 2*p*(1+(1/(4*n)))
#    p = 2*p*(1+1/4*n-3/32*n**2)
#    p = 2*p*(1+(1/(4*n))-(3/(32*n**2))+(3/(128*n**3)))
    return (p)
#print("PiWallis=", PiWallis(100))
#print("Pi exact=", pi)