#%%
def starts_with(string,list_words,other=None):
    if other==None:
        other = []
    
    for word in list_words:
        if string.startswith(word):
            other.append(word)
            return starts_with(string[len(word):],list_words,other)
    return other

print(starts_with('iamsahilkatkar',['sahil','katkar','i','am']))
# %%
# 