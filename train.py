import torch
import time

device = torch.device("cuda")

start = time.time()

x = torch.rand(5000, 5000).to(device)
y = torch.rand(5000, 5000).to(device)

z = torch.matmul(x, y)

torch.cuda.synchronize()

print("Completed on:", z.device)
print("Time:", time.time() - start)