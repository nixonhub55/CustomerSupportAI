from dataclasses import dataclass, field


@dataclass
class Action:

    tool: str

    args: dict = field(default_factory=dict)

    intent: str = "UNKNOWN"