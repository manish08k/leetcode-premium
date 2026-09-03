class Solution:
    def sortArray(self, nums: List[int]) -> int:
        def A():
            ans = 0
            for ii in range(len(nums)):
                if nums[ii] == 0:
                    ind_zero = ii
                    break
            val_ind = {}
            for ii in range(len(nums)):
                if nums[ii] != 0 and nums[ii] != ii:
                    val_ind[nums[ii]] = ii
            while ind_zero != 0:
                ans += 1
                h = ind_zero
                ind_zero = val_ind[ind_zero]
                del val_ind[h]
            ans += len(val_ind.keys())
            vis = set()
            for x in val_ind.keys():
                if x not in vis:
                    ans += 1
                    while x not in vis:
                        vis.add(x)
                        x = val_ind[x]
            return ans
        # [1,2,3,0] sort
        def B():
            ans = 0
            for ii in range(len(nums)):
                if nums[ii] == 0:
                    ind_zero = ii
                    break
            val_ind = {}
            for ii in range(len(nums)):
                if nums[ii] != 0 and nums[ii] != ii + 1:
                    val_ind[nums[ii]] = ii
            while ind_zero != len(nums)-1:
                ans += 1
                h = ind_zero
                ind_zero = val_ind[ind_zero+1]
                del val_ind[h+1]
            ans += len(val_ind.keys())
            vis = set()
            for x in val_ind.keys():
                if x not in vis:
                    ans += 1
                    while x not in vis:
                        vis.add(x)
                        x = val_ind[x] + 1
            return ans
        return min(A(),B())