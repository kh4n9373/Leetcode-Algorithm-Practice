from dataclasses import dataclass
from functools import partial
from typing import List

from returns.pipeline import flow, pipe
from returns.pointfree import bind, cond
from returns.result import Result, ResultE
from lambdas import _


@dataclass
class Matrix:
    data: List[List[float]]


class MatrixTrait:
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
                    lambda first_row_leng: partial(
                        map, lambda row: len(row) == first_row_leng
                    ),
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
