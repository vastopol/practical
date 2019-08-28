def next_version(version):
    nums = [int(s) for s in reversed(version.split('.'))]
    if len(nums) == 1:
        return str(nums[0]+1)
    carry = False
    amount = len(nums)
    for n in range(amount):
        if n+1 == amount and carry:    # last
            nums[n] += 1
            break
        elif n == 0 and nums[n] < 9:   # first
            nums[n] += 1
            break
        elif nums[n] == 9:
            nums[n] = 0
            carry = True
        elif carry:
            nums[n] += 1
            carry = False
        if not carry:
            break
    new_ver = '.'.join(map(str,reversed(nums)))
    return new_ver
