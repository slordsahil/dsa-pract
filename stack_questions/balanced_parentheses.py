def balanced_parenthese(s):
    openings =set('([{')
    matching_parentheses =([('(',')'),('[',']'),('{','}')])

    stack=[]
    for i in s:
        if i in openings:
            stack.append(i)
        else:
            if stack==[]:
                return False
            
            elif (stack[-1],i) in matching_parentheses:
                stack.pop()
            else:
                return False
    return len(stack)==0
            
        
        
a=balanced_parenthese('()]')   
print (a)