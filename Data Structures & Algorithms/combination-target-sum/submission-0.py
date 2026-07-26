class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        '''
        for every elem in list, we r deciding if we should keep it or not
        this we create a decision tree
        and we can use recursive dfs to iterate thru all decisions


        res = []
        defs:
            base case 1: found target
            base case 2: invalid combo (i >= bounds OR total > target)

            2 decisions:
            add candidate[i] + dfs that tree
            don't include candidate[i] + dfs that tree

        call dfs the first time
        return res 
        '''

        res = []
        def dfs(i, curr, total):
            
            if total == target:
                res.append(curr.copy())
                return
            if (i >= len(nums)) or (total > target):
                return

            curr.append(nums[i])
            dfs(i, curr, total + nums[i])

            curr.pop()
            dfs(i+1, curr, total)
        
        dfs(0, [], 0)
        return res