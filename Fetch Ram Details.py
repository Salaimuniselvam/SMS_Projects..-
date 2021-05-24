import psutil

def get_size(bytes,suffix="B"):
	factor=1024
	for unit in ["","K","M","G","T","P"]:
		if bytes< factor:
			return f"{bytes:2f}{unit}{suffix}"
			bytes/= factor

#Get the memory details..
svmem=psutil.virtual_memory()
print(f"Total:{get_size(svmem.total)}")
print(f"used:{get_size(svmm.used)}")
print(f"percentage:{svmm.percent}%")

#Get the swap memory details (if exists)
swap=psutil.swap_memory()
print("/n swap partition :")
print(f"Total:{get_size(swap.total)}")
print(f"Free:{get_size(swap.free)}")
print(f"Used:{get_size(swap.used)}")
print(f"percentage:{swap.percent}%")