# check i f palidrome ?

def palidrome(sentence):
#     reverse=[]
#     sentence=sentence.split()
#     x=len(sentence)
#     print(sentence)

#     for i in range((x-1),-1,-1):
        
#         sentence[i]=sentence[i].split(" ")
#         k=len(sentence[i])
#         print (sentence[i])
#     for j in range((k-1),-1,-1):
#         print(sentence[j])
#         reverse.append(sentence[j])
#     print(reverse)
#     if sentence==reverse:
#         return True
#     else:
#         return False

# print(palidrome("Red rum  sir is murder"))

    s1=sentence.lower().replace(" ","")
    s2=s1.split(" ")
    #s2=s1.join( )
    
    if s2[::1]==s2[::-1]:
        return "palidrome"
    else:
        return "false"
print(palidrome("Red rum  sir is murder"))