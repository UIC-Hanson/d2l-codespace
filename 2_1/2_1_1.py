import torch
x = torch.arange(12, dtype=torch.float32)
print(x)
print(x.numel())
print(torch.Size([12]))
X = x.reshape(3, 4)
print(X)