from copy import copy
from functools import partial
from typing import Dict, List, final

from lambdas import _
from returns.maybe import Maybe
from returns.pipeline import flow
from returns.pointfree import bind, cond, map_
from returns.result import Result, ResultE, safe

from mathy.algebra.matrix.type import IMatrixTrait, Matrix
from mathy.algebra.vector.trait import VecTrait
from mathy.algebra.vector.type import Vec


@final
class MatrixTrait(IMatrixTrait):

    @staticmethod
    def row_space_dim(mat: Matrix) -> int:
        return flow(mat.data, _[0], len)

    @staticmethod
    def col_space_dim(mat: Matrix) -> int:
        return flow(mat.data, len)

    @staticmethod
    @safe
    def mat2rowdict(mat: Matrix) -> Dict[str, Vec]:
        col_labels = [indice for indice in list(range(MatrixTrait.row_space_dim(mat)))]
        row_labels = [indice for indice in list(range(MatrixTrait.col_space_dim(mat)))]
        set_col_labels = set(flow(col_labels, partial(map, str)))
        return {
            str(c): VecTrait.parse(
                set_col_labels, {str(r): mat.data[c][r] for r in col_labels}
            ).unwrap()
            for c in row_labels
        }

    @staticmethod
    def linear_com_to_a_row(
        mat: Matrix,
        row_des_ind: int,
        row_ap_ind: int,
        row_des_coe: float,
        row_ap_coe: float,
    ) -> ResultE[Matrix]:
        return flow(
            mat,
            MatrixTrait.col_space_dim,
            _ > row_des_ind and _ > row_ap_ind,
            cond(Result, mat.data, Exception("ROW_INDEX_INCORRECT")),
            map_(copy),
            map_(
                _[:row_des_ind]
                + [
                    [
                        row_des_coe * t[0] + row_ap_coe * t[1]
                        for t in zip(_[row_des_ind], _[row_ap_ind])
                    ]
                ]
                + _[(row_des_ind + 1) :]
            ),
            map_(MatrixTrait.parse),
        )

    @staticmethod
    def swap_row(mat: Matrix, row_ind: int, other_row_ind: int) -> ResultE[Matrix]:
        def swap_row_proc(data: List[List[float]], row_ind: int, other_row_ind: int):
            update_data = copy(data)
            update_data[row_ind], update_data[other_row_ind] = (
                update_data[other_row_ind],
                update_data[row_ind],
            )
            return update_data

        return flow(
            mat,
            MatrixTrait.col_space_dim,
            _ > row_ind and _ > other_row_ind,
            cond(Result, mat.data, Exception("ROW_IND_INCORRECT")),
            map_(lambda data: swap_row_proc(data, row_ind, other_row_ind)),
            bind(lambda updated_data: MatrixTrait.parse(updated_data)),
        )

    @staticmethod
    def row(mat: Matrix, ind: int):
        labels = [str(i) for i in range(MatrixTrait.row_space_dim(mat))]
        return flow(
            ind,
            _ < MatrixTrait.col_space_dim(mat),
            cond(Maybe, mat.data[ind]),
            map_(
                lambda vec_arr: VecTrait.parse(set(labels), dict(zip(labels, vec_arr))).unwrap()
            ),  # panic, not good
        )
