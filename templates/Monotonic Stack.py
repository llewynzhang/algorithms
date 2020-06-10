# forward
def next_greater_element(nums: List[int]) -> List[int]:
	res = [-1] * len(nums)
	stack = []
	for i in range(len(nums)):
		while stack and nums[i] > nums[stack[-1]]:
			index = stack.pop()
			res[index] = nums[i]
		stack.append(i)
	return res

# backward
def next_greater_element(nums: List[int]) -> List[int]:
	res = [-1] * len(nums)
	stack = []
	for i in reversed(range(len(nums))):
		while stack and nums[i] >= stack[-1]:
			stack.pop()
		res[i] = stack[-1] if stack else -1
		stack.append(nums[i])
	return res