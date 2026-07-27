
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mat=set()
        for num in nums:
            if num in mat:
                return True
            mat.add(num)
        return False
            