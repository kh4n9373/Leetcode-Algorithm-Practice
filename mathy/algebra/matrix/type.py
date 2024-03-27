from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import partial
from typing import Dict, List

from lambdas import _
from returns.maybe import Maybe
from returns.pipeline import flow, pipe
from returns.pointfree import bind, cond
from returns.result import Result, ResultE

from mathy.algebra.vector.type import Vec


@dataclass
class Matrix:
    data: List[List[float]]


class IMatrixTrait(ABC):
    empty_matrix_exception_code = "MATRIX_EMPTY"
    dispution_row_dim_matrix_exception_code = "ROW_DISPUTE_DIM"

    @classmethod
    def parse(cls, data: List[List[float]]) -> ResultE[Matrix]:

        return flow(
            data,
            len,
            _ > 0,
            cond(Result, data, Exception(cls.empty_matrix_exception_code)),
            bind(
                pipe(
                    _[0],
                    len,
                    lambda first_row_leng: partial(map, lambda row: len(row) == first_row_leng),
                    lambda m: m(data),
                    all,  # is all row length is same with first_row_length ?
                    cond(
                        Result,
                        Matrix(data),
                        Exception(cls.dispution_row_dim_matrix_exception_code),
                    ),
                )
            ),
        )

    @staticmethod
    @abstractmethod
    def row_space_dim(mat: Matrix) -> int:
        pass

    @staticmethod
    @abstractmethod
    def col_space_dim(mat: Matrix) -> int:
        pass

    @staticmethod
    @abstractmethod
    def mat2rowdict(mat: Matrix) -> ResultE[Dict[str, Vec]]:
        pass

    @staticmethod
    @abstractmethod
    def linear_com_to_a_row(
        mat: Matrix,
        row_des_ind: int,
        row_ap_ind: int,
        row_des_coe: float,
        row_ap_coe: float,
    ) -> ResultE[Matrix]:
        pass

    @staticmethod
    @abstractmethod
    def swap_row(mat: Matrix, row_ind: int, other_row_ind: int) -> ResultE[Matrix]:
        pass

    @staticmethod
    @abstractmethod
    def row(mat: Matrix, ind: int) -> Maybe[Vec]:
        pass
