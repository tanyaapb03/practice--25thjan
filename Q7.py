# merge all overlapping intervals

def mer (intervals):
    intervals=sorted([intervals])
    new_list=[]
    start=intervals[0][0][0]
    end =intervals[0][0][1]
    print(start,end )
    for i in intervals[0][1:]:
        print(i)
        
        if i[0]>=start and i[0]<=end :
            if i[1]>= start and i[1]<=end :
                start=start
                end=end
        else: 

            if i[0]>=start and i[0]<=end :
                if i[1]>= start and i[1]>=end :
                    end = intervals[i][1]
        
            else:
                if i[0]>=start and i[0]>=end :
                    if i[1]>= start and i[1]>=end :
                        start= intervals[i[0]]
                        end=intervals[i[1]]
            
        print (i)
        new_list.append([start,end])
    return new_list
array=[[1,4],[3,6],[7,8]]
print(mer(array))