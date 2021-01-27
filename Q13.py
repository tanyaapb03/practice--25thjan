# check if parenthesis are balanced 

def balanced(exp):
    open_braces=tuple("{([")
    closing_braces=tuple("})]")
    map=dict(zip(open_braces,closing_braces))
    queue=[]
  


    
    
    for char in exp:
        
        if char in open_braces:
            queue.append(map[char])
        else:
            if char in closing_braces:
                print(queue.append(map[char]))
            if not queue or char != queue.pop():
                return "unbalanced"
        print(queue)
        if not queue:
            return " unbalanced"
        else:
            return "balanced"

print(balanced(["[","{","}"]))