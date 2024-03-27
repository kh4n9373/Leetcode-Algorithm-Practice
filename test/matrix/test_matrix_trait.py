from returns.maybe import Maybe, Some
from returns.result import Failure, Success

from mathy.algebra.matrix.trait import MatrixTrait
from mathy.algebra.matrix.type import IMatrixTrait, Matrix
from mathy.algebra.vector.type import Vec


def test_parser_normal(matrix_trait: IMatrixTrait) -> None:
    result_normal = matrix_trait.parse([[0, 1, 2], [-1, 0, 1], [-2, -1, 0], [-3, -2, -1]])
    match result_normal:
        case Success(Matrix()):
            assert True
        case _:
            assert False


def test_parser_empty(matrix_trait: IMatrixTrait) -> None:
    fail_1 = matrix_trait.parse([])
    match fail_1:
        case Failure(Exception() as e):
            assert str(e) == MatrixTrait.empty_matrix_exception_code
        case _:
            assert False


def test_dispution_dim(matrix_trait: IMatrixTrait) -> None:
    fail_1 = matrix_trait.parse([[0, 2, 1], [1, 2]])
    match fail_1:
        case Failure(Exception() as e):
            assert str(e) == matrix_trait.dispution_row_dim_matrix_exception_code
        case _:
            assert False


def test_dim_retrieve(matrix_trait: IMatrixTrait) -> None:
    mat = matrix_trait.parse([[0, 1, 2], [-1, 0, 1], [-2, -1, 0], [-3, -2, -1]]).unwrap()
    assert matrix_trait.row_space_dim(mat) == 3
    assert matrix_trait.col_space_dim(mat) == 4


def test_mat2rowdict(matrix_trait: IMatrixTrait) -> None:
    mat = matrix_trait.parse([[0, 1, 2], [-1, 0, 1], [-2, -1, 0], [-3, -2, -1]]).unwrap()
    rowdict = matrix_trait.mat2rowdict(mat).unwrap()
    assert isinstance(rowdict["0"], Vec)
    assert rowdict["0"].D == set(("0", "1", "2"))


def test_swap_row(matrix_trait: IMatrixTrait) -> None:
    mat = MatrixTrait.parse([[0, 1, 2], [-1, 0, 1], [-2, -1, 0], [-3, -2, -1]]).unwrap()
    updated_mat_result = MatrixTrait.swap_row(mat, 0, 3)
    labels = ["0", "1", "2"]
    match updated_mat_result:
        case Success(updated_mat):
            assert Maybe.do(
                vec1 == vec2
                for vec1 in matrix_trait.row(updated_mat, 0)
                for vec2 in matrix_trait.row(mat, 3)
            ) == Some(True)
            assert Maybe.do(
                vec1 == vec2
                for vec1 in matrix_trait.row(updated_mat, 0)
                for vec2 in matrix_trait.row(mat, 3)
            ) == Some(True)
            assert matrix_trait.row(updated_mat, 3).unwrap().f == dict(zip(labels, mat.data[0]))
        case _:
            assert False


# def test_linear_com_rows(matrix_trait: IMatrixTrait):
#     mat = MatrixTrait.parse([[0, 1, 2], [-1, 0, 1], [-2, -1, 0], [-3, -2, -1]]).unwrap()
