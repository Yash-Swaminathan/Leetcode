class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        #hashmap probably store which elements are seen the most 
        # once seen store number then go to next 
        # could maybe split once newest element but will take too long
        # another thing we could do is sort the array then calculate index first seen at and last seen at
        # built in pyhton function called most_common to return this

        # hashmap to store how many times it appears
        count = {}
        #create empty list for however many numbers are in nums [[], [], [], [], [], []]
        freq = [[] for i in range(len(nums) + 1)]
        # count we are looking for store in hshmap
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # store into frequency buckets [[], [], [], [], [], []]
        for n, c in count.items():
            freq[c].append(n)
            # final result
        res = []
        for i in range(len(freq) - 1, 0, -1): # high to low
            for n in freq[i]: #
                res.append(n)
                # stop when we have 'k' numbers
                if len(res) == k:
                    return res