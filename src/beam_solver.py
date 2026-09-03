from dataclasses import dataclass, field
from typing import Callable, Optional

@dataclass
class PointForce:
    position: float
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


class Beam:
    def __init__(self, length: float):
        self.length = length
        self.point_forces: list[PointForce] = []
        self.point_moments: list[PointMoment] = []
        self.distributed_loads: list[DistrubutedLoad] = []

    def add_point_force(
            self, 
            position: float, 
            magnitude: float
        ) -> PointForce:
        
        if position < 0 or position > self.length:
            raise ValueError("Position must be within beam length")

        force = PointForce(position, magnitude)

        self.point_forces.append((force))

        return force

    def add_point_moment(
            self, position: float, magnitude: float) -> PointMoment:
        if position < 0 or position > self.length:
            raise ValueError("Position must be within beam length")

        moment = PointMoment(position, magnitude)

        self.point_moments.append(moment)

        return moment

    def add_distrubuted_load(
            self, 
            start_position: float,
            end_position: float, 
            func: Optional[Callable[[float], float]] = None,
            start_magnitude: Optional[float] = None,
            end_magnitude: Optional[float] = None,
            args: tuple = (),
            kwargs: dict = None
    ) -> DistrubutedLoad:

        if kwargs is None:
            kwargs = {}

        if start_position < 0 or end_position > self.length:
            raise ValueError("Start and end positions must be within beam length")

        dist_loat = DistrubutedLoad(
            start_position=start_position,
            end_position=end_position,
            func=func,
            start_magnitude=start_magnitude,
            end_magnitude=end_magnitude,
            args=args,
            kwargs=kwargs
        )

        self.distributed_loads.append(dist_loat)
        return dist_loat

    