from typing import final
from math.algebra.vector.type import IVecTrait, Vec
from toolz.dicttoolz import valmap
from returns.result import Result
from returns.pointfree import cond


@final
class VecTrait(IVecTrait):
    @staticmethod
    def scalar_mul(v: Vec, alpha: float):
        return Vec(v.D, dict(zip(v.f.keys(), [v.f[key] * alpha for key in v.f.keys()])))

    @staticmethod
    def check_if_same_domain(v: Vec, u: Vec):
        return len(v.D) == len(u.D)

    @staticmethod
    def add(v: Vec, u: Vec):
        def with_have_same_domain():
            list_key = list(v.D)
            return Vec(
                v.D,
                dict(
                    zip(
                        list_key,
                        [v.f.get(key, 0) + u.f.get(key, 0) for key in list_key],
                    )
                ),
            )

        return cond(
            Result,
            with_have_same_domain(),
            Exception(
                "input vectors are not able to add to each other, because they are not setteld in the domain dimension"
            ),
        )(VecTrait.check_if_same_domain(v, u))

    @staticmethod
    def neg(v: Vec):
        return Vec(v.D, valmap(lambda v: -v, v.f))
