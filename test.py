import torch
print("CUDA Available:", torch.cuda.is_available())  # Should return True
print("CUDA Device Count:", torch.cuda.device_count())  # Should return the number of GPUs
print("Current Device Name:", torch.cuda.get_device_name(0))  # Should print your GPU name


