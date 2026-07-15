from core.container import Container


class Repository:

    def __init__(self):

        print("Repository created")


class Service:

    def __init__(
        self,
        repository: Repository
    ):

        print("Service created")

        self.repository = repository


container = Container()

repo = container.resolve(
    Repository
)

service = container.resolve(
    Service
)

print(
    service.repository is repo
)