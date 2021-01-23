class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        seqs = [[nums[0]]]
        current = nums[0]
        idx = 1
        while idx < len(nums):
            if nums[idx] == current:
                seqs.append([current])
                idx += 1
            elif nums[idx] == current + 1:
                current += 1
                seqidx = len(seqs) - 1
                while seqidx >= 0 and seqs[seqidx][-1] == current - 1 and idx < len(nums) and nums[idx] == current:
                    seqs[seqidx].append(current)
                    seqidx -= 1
                    idx += 1
            else:
                seqs.append([nums[idx]])
                current = nums[idx]
                idx += 1
        for seq in seqs:
            if len(seq) < 3:
                return False
        return True