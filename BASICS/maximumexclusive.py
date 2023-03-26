num=input("Enter the numbers:")
nums=list(num.split(","))
length=len(nums)
for a in range(length):
    if type(nums[a])==<class 'int'>:
        s=[int(x) for x in nums]
        s.sort()
        n=len(s)
        print("Max of given numbers is:",s[n-1])
