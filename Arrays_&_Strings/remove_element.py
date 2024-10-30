def removeElement(nums: List[int], vaL: int) -> int:
    j = 0
    for i in range(len(nums)):
        if nums[i] != vaL:
            nums[j] = nums[i]
            j += 1
    return j
