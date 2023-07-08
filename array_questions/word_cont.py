#%%
strin='AAaAA'
def word_cont(string):
    string=sorted(string)
    string_char=[]
    cnt=0
    for i in string:
        if i in string_char:
            cnt+=1
        else:
            if cnt!=0:
                string_char.append(str(cnt))
            string_char.append(i)
            cnt=1
    string_char.append(str(cnt))
    
    return ''.join(string_char)
    
    
    
word_cont = word_cont(strin)
print(word_cont)
    
# %%
