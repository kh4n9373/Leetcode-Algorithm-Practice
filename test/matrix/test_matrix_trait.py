from returns.result import Failure, Success
from mathy.algebra.matrix.type import Matrix, MatrixTrait


def test_parser_normal():
    result_normal = MatrixTrait.parse(
        [[0, 1, 2], [-1, 0, 1], [-2, -1, 0], [-3, -2, -1]]
    )
    match result_normal:
        case Success(Matrix()):
            assert True
        case _:
            assert False


def test_parser_empty():
    fail_1 = MatrixTrait.parse([])
    match fail_1:
        case Failure(Exception() as e):
            assert str(e) == MatrixTrait.empty_matrix_exception_code
        case _:
            assert False


def test_dispution_dim():
    fail_1 = MatrixTrait.parse([[0, 2, 1], [1, 2]])
    match fail_1:
        case Failure(Exception() as e):
            assert str(e) == MatrixTrait.dispution_row_dim_matrix_exception_code
        case _:
            assert False
