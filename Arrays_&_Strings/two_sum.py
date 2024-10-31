def twoSum(num: List[int], target: int) -> List[int]:
    i, j = 0, len(num) - 1
    
    while i < j:
        total = num[i] + num[j]
        if total == target:
            return [i + 1, j + 1]
        elif total < target:
            i += 1
        else:
            j -= 1
