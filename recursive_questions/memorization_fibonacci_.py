mem={}
def fib(N):
    if N in mem:
        return mem[N]
    elif N<2:
        value =N
    else:
        value=fib(N-1) + fib(N-2)
    mem[N] = value
    return value

a=fib(190)
print(a)
# %%
