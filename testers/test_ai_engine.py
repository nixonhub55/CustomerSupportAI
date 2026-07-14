from framework.kernel import Kernel

kernel = Kernel()

kernel.boot()

assistant = kernel.get_assistant("billing")

print(type(assistant).__name__)