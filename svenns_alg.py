def func(x):
    return x**2+6*x+12

def sven(x, step):
    prev = func(x - step)
    cur = func(x)
    next = func(x + step)
    if prev >= cur and cur <= next:
        return(f"L=[{func(x - step)}; {func(x + step)}]")
    
    if prev <= cur and cur >= next: 
        return("Результат не может быть найден с текущими параметрами")
    
    if prev >= cur and cur >= next:
        temp  = sven_step(x + step, step, None)
        first = x if temp[1] == None else temp[1]
        last = temp[0]
        return first, last
    
    if prev <= cur and cur <= next:
        temp  = sven_step(x, -1*step, None)
        first = temp[0]
        last = x if temp[1] == None else temp[1]
        return first, last
        
        
def sven_step(x, step, change):
    cur = x
    next = x + step

    if func(next) < func(cur):
        
        change = cur
        return sven_step(next, step, change)

    return next, change

print(sven(-10, 2))
print(sven(1, 2))
print(sven(1, 1))
print(sven(0, 1))