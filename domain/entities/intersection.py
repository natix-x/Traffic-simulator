import uuid
from dataclasses import dataclass, field


@dataclass
class Intersection:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
