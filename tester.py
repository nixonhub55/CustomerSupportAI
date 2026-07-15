from core.lifecycle import Lifecycle

life = Lifecycle()

life.on_startup(
    lambda: print("Config")
)

life.on_startup(
    lambda: print("Plugins")
)

life.on_shutdown(
    lambda: print("Stopping")
)

life.startup()

life.shutdown()