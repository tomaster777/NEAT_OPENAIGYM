from typing import Tuple
from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class Innovation():
    idx: int
    src: int
    dst: int
    weight: float
    enabled: bool


class NodeType(Enum):
    INPUT = 'input'
    HIDDEN = 'hidden'
    OUTPUT = 'output'


@dataclass(frozen=True)
class Node:
    idx: int
    role: NodeType


@dataclass(frozen=True)
class Genome:
    nodes: Tuple[Node]
    innovations: Tuple[Innovation]
