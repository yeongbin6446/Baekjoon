s = input()
s = s.split('-')
nums = []
for i in s:
    nums.append(i.split('+'))

for i in range(len(nums)):
    for j in range(len(nums[i])):
        idx = 0
        if nums[i][j][0] == '0':
            while nums[i][j][idx] == '0':
                idx += 1
            nums[i][j] = nums[i][j][idx:]

ans = []
for i in nums:
    ans.append(sum(list(map(int,i))))

answer = ans[0]
for i in range(1,len(ans)):
    answer -= ans[i]

print(answer)
