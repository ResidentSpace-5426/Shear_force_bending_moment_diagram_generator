from dataclasses import dataclass, field
from typing import Callable, Optional

@dataclass
class PointForce:
    postion: float
    magnitude: float

@dataclass
class PointMoment:
    postion: float
    magnitude: float   

@dataclass
class DistrubutedLoad:
    # Start and end positions of the load
    start_position: float
    end_position: float

    func: Optional[Callable[[float], float]] = None
    start_magnitude: Optional[float] = None
    end_magnitude: Optional[float] = None

    args: tuple = field(default_factory=tuple)
    kwargs: dict = field(default_factory=dict)

    def __post_init__(self):
        if self.func is not None:
            return

        if self.start_magnitude is not None and self.end_magnitude is not None:
            if self.start_position == self.end_position:
                raise ValueError("Start and stop cannot be the same value")

            if self.start_magnitude == self.end_magnitude:
                self.func = lambda x: self.start_magnitude
                return

            else:
                y0, y1 = self.start_magnitude, self.end_magnitude
                x0, x1 = self.start_position, self.end_position

                self.func = lambda x: y0 + (x - x0) * (y1 - y0) / (x1 - x0)
                return

        raise ValueError("Either func or start_magnitude and end_magnitude must be provided")

    def eval_at(self, position: float) -> float:
        if position < self.start_position or position > self.end_position:
            return 0.0

        return self.func(position, *self.args, **self.kwargs)

