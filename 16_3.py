def r_max(args):
    largest= float('-inf')
    for item in args:
        # i googled this part,I was lost
        if isinstance(item,list):
            largest =max(largest,r_max(*item))
        else:
            largest = max(largest,item)

    return largest 


nested_numbers =[1,[2,3],[4,[5,6]]]