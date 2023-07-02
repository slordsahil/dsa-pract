
def find_themissing_element(ori_list,edited_list):
    edited_list.sort()
    for i in range(len(ori_list)):
        if ori_list[i] != edited_list[i]:
            return ori_list[i]
        
missing_no=find_themissing_element([1,2,3,4,5,6,7],[3,7,2,1,4,6])
print (missing_no)
