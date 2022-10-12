def calculate(min, max, step):
    result=0
    for n in range(min, max+1, step):
        result=result+n
    print(result)
# 請用你的程式補完這個函式的區塊
calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0

def avg(data):
    employees=data["employees"]
    sum=0
    number=0
    for n in employees:
        manager=n["manager"] #取出manager的值
        if manager==False:
            salary=n["salary"] #取出salary的值
            sum=sum+salary
            number+=1
    print(sum/number)
            
avg({
    "employees":[
        {
            "name":"John",
            "salary":30000,
            "manager":False
        },
        {
            "name":"Bob",
            "salary":60000,
            "manager":True
        },
        {
            "name":"Jenny",
            "salary":50000,
            "manager":False
        },
        {
            "name":"Tony",
            "salary":40000,
            "manager":False
        }
    ]
}) # 呼叫 avg 函式

def func(a):
    def add(b,c):
        print(b*c+a)
    return add
func(2)(3, 4)# 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# # 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

def maxProduct(nums):
    n = len(nums)
    New = []
    for x in range(n):
        for y in range(x+1,n):
            num = nums[x] * nums[y]
            New.append(num)
    print(max(New))

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10

def twoSum(nums, target):
  n = len(nums)
  for x in range(n):
    for y in range(x+1,n):
      if (target == nums[x] + nums[y]):
        return [x, y]
  
result = twoSum([2, 11, 7, 15], 9)
print(result)  # show [0, 2] because nums[0]+nums[2] is 9

def maxZeros(nums):
    count = 0
    Newnums = []
    for x in nums:
        if x == 0:
            count += 1
            Newnums.append(count)
        else:
            Newnums.append(0)
            count = 0
    print(max(Newnums))

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3
