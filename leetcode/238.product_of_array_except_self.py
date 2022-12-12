def product_except_self(nums):
    output = [1] * len(nums)

    prefix = 1
    for indx in range(len(nums)):
        output[indx] = prefix
        prefix *= nums[indx]

    postfix = 1
    for indx in range(len(nums) - 1, -1, -1):
        output[indx] *= postfix
        postfix *= nums[indx]

    return output
