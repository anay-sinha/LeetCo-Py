class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        path = []
        res = []
        candidates.sort()

        def recurse(i, total):
            if total == target:
                res.append(path[:])
                return
            
            if i >= len(candidates):
                return
            
            if total + candidates[i] > target:
                return
            path.append(candidates[i])
            recurse(i, total + candidates[i])
            path.pop()

            recurse(i+1, total)
        
        recurse(0,0)
        
        return res