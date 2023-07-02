#%%%
s='hi i am sahil vijay      katkar       '
def reverse_string(s):
    return ' '.join(reversed(s.split()))
    # reverse_string =[]
    # splited_string=s.split(' ')
    # for i in range(1,len(splited_string)+1):
    #     if splited_string[-i] =='':
    #         splited_string[-i].replace(' ',',')
    #         continue
    #     reverse_string.append(splited_string[-i])
    # return ' '.join(reverse_string)
a=reverse_string(s)
print(a)
# %%
