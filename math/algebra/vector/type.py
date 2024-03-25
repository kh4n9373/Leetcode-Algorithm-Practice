from abc import ABC, abstractmethod
import json
from typing import Dict
from returns.pointfree import bind, cond

from returns.result import Result, ResultE
from returns.pipeline import flow


class Vec:
    def __init__(self, labels: set[str], function: Dict[str, float]):
        self.D = labels
        self.f = function

    def __repr__(self):
        return json.dumps({"domain": list(self.D), "function": self.f})


class IVecTrait(ABC):

    # smart parser (smart constructor)
    @staticmethod
    def parse(labels: set[str], function: Dict[str, float]):
        def is_same_dimension():
            return len(labels) == len(function)

        def is_same_var():
            return all([key in function for key in labels])

        def construct():
            return Vec(labels, function)

        return flow(
            is_same_dimension(),
            cond(
                Result,
                construct(),
                Exception("domains and functions does not contains the same dimension"),
            ),
            bind(
                lambda r: cond(
                    Result,
                    r,
                    Exception("function lacks some of project for some var in domain"),
                )(is_same_var())
            ),
        )

    @abstractmethod
    def scalar_mul(self, vec: Vec, alpha: float) -> Vec:
        pass

    @staticmethod
    @abstractmethod
    def check_if_same_domain(vec: Vec, other: Vec) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def add(vec: Vec, other: Vec) -> ResultE[Vec]:
        pass

    @staticmethod
    @abstractmethod
    def neg(vec: Vec) -> Vec:
        pass
