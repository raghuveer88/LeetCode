class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        temp = chars[0]
        count = 0
        result = []
        for i in chars:
            if i == temp:
                count += 1
            elif i != temp:
                result.append(temp)    
                if count <10 and count>1:
                    result.append(str(count))
                elif count > 1:
                    for j in str(count):
                        result.append(j)
                        print(j)
                temp = i
                count = 1
        if count>1 and count <10:
            result.extend([temp,str(count)])
        elif count > 1:
            result.append(temp)
            for j in str(count):
                result.append(j)
        elif count ==1:
            result.append(temp)
                
        
        for i in range(len(result)):
            chars[i] = result[i]
        return len(result)
            