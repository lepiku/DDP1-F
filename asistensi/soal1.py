def k_sum_pairs(a_list,k):
    result = []
    for i in a_list:
        for j in a_list:
            test_sum = i + j
            if(test_sum == k):
                result.append((i,j))
    
    print (result)
    return result

k_sum_pairs([-4,5,-2,7],-8)
k_sum_pairs([-4,5,-2,7],2)