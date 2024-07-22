import torch 
import pandas
'''
# 基本操作
x = torch.arange(12)
x.reshape(3,4)
print(x.shape)

y = torch.zeros(2,3,4)
print(y)

z = torch.ones(3,2,1)
print(z)

a = torch.randn(3,4,2)
print(a)

b = [i for i in range(100)]
print(b)
b = torch.tensor(b).reshape(10,-1)
print(b)

# 运算
x = torch.randn(3,4)
y = torch.randn(3,5)
z = 3
print(x)
print(y)
print(x + y)

# 连接
x = torch.arange(12).reshape(3,4)
y = torch.arange(12,24).reshape(3,4)
z = torch.cat((x, y),dim=-2)
print(x, y, z)
print(x == y)

# 广播机制
x = torch.arange(12).reshape(-1,1)
y = torch.arange(12).reshape(1,-1)
print(x + y)
'''

x = torch.arange(12).reshape(3,4)
y = x.T
print(torch.mm(x, y))
print(x.shape)