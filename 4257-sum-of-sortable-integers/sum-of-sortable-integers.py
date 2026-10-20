class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k:
                continue

            ok = True
            prev_max = None

            for s in range(0, n, k):
                e = s + k
                mn = mx = nums[s]
                desc = 0

                for i in range(s + 1, e):
                    x = nums[i]
                    mn = min(mn, x)
                    mx = max(mx, x)

                    if nums[i - 1] > x:
                        desc += 1
                        if desc > 1:
                            ok = False
                            break

                if not ok:
                    break

                if desc == 1 and nums[e - 1] > nums[s]:
                    ok = False
                    break

                if prev_max is not None and prev_max > mn:
                    ok = False
                    break

                prev_max = mx

            if ok:
                ans += k

        return ans