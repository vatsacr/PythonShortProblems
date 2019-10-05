sample_list = [5,4,3,7,8,3,4,6,5,3,2,5,8,8,4,3,2,2]
def has_sublist(get_list):
    count=0
    for iterator in sample_list:
        if(isinstance(iterator,list)):
            count+=1
    else:
            count+=0

    if(count>0):
        print ('It is {0} that {1} has a sublist'.format(count>0,sample_list))
    else:
        print ('It is {0} that {1} has a sublist'.format(count>0,sample_list))
has_sublist(sample_list)
