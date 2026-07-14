from framework.kernel import Kernel

kernel = Kernel()

kernel.boot()

print(kernel.get_assistant("billing"))