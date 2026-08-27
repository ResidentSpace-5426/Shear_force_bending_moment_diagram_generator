from dataclasses import dataclass

@dataclass
class PointForce:
    postion: float
    magnitude: float

@dataclass
class PointMoment:
    postion: float
    magnitude: float   

@dataclass
class LinearDistrubutedLoad:
    start_postion: float
    end_postion: float
    start_magnitude: float
    end_magnitude: float

    def magnitude_at(self, position: float) -> float:
        if position < self.start_postion or position > self.end_postion:
            return 0.0
        else:
            # Linear interpolation between start and end magnitudes
            slope = (self.end_magnitude - self.start_magnitude) / (self.end_postion - self.start_postion)
            return self.start_magnitude + slope * (position - self.start_postion)

@dataclass
class EquationDistrubutedLoad:
    start_postion: float
    end_postion: float
    equation: str  # This should be a string representing the equation

    def magnitude_at(self, position: float) -> float:
        if position < self.start_postion or position > self.end_postion:
            return 0.0
        else:
            # Evaluate the equation at the given position
            # Note: Using eval can be dangerous; ensure the input is sanitized in a real application
            return eval(self.equation.replace('x', str(position)))


