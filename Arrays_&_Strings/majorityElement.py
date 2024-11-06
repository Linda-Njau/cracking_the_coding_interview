def majorityElement(nums: List[int]) -> int:
    count = {}
    res = majority = 0
    
    for i in nums:
        count[i] = count.get(i, 0) + 1
        if count[i] > majority:
            res = i
            majority = count[i]
    return res
