// 1812 ms | 13.4 MB
class Solution :
    def twoSum(self, param_1, param_2) :
        for i in range(len(param_1)) :
            for j in range(i+1, len(param_1)) :
                if param_1[i]+param_1[j] == param_2 :
                    return[i,j]
