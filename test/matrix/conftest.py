import pytest

from mathy.algebra.matrix.trait import MatrixTrait


@pytest.fixture()
def matrix_trait():
    yield MatrixTrait
