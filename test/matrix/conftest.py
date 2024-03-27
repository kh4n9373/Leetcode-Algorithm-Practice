from collections.abc import Generator
from typing import Any

import pytest

from mathy.algebra.matrix.trait import MatrixTrait
from mathy.algebra.matrix.type import IMatrixTrait


@pytest.fixture()
def matrix_trait():
    yield MatrixTrait
