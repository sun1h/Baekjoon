def solution(s):
    nums = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7'
        , 'eight': '8', 'nine': '9', 'zero': '0'}

    lst = []
    res = []
    for i in range(len(s)):

        if s[i].isalpha():
            lst.append(s[i])
            tmp = ''.join(lst)

            if nums.get(tmp) :
                res.append(nums[tmp])
                lst = []
            else:
                continue

        else:

            res.append(str(s[i]))

    answer = int(''.join(res))

    return answer