import torch

print(torch.__version__)
print(torch.version.hip if hasattr(torch.version, "hip") else "No HIP support")
print(torch.cuda.is_available())
print(torch.cuda.device_count())
print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No CUDA GPU")
