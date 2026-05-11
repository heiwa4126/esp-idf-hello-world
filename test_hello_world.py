# pytest_hello_world.py がややこしいので最小限のテストにしたもの

import pytest
from pytest_embedded_idf.dut import IdfDut


@pytest.mark.parametrize("target", ["esp32"], indirect=True)
def test_hello_world(dut: IdfDut) -> None:
    dut.expect_exact("Hello world!")
