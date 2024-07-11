from Base.Libraries.uart_stm import uart_py
import logging
import pytest

@pytest.fixture(scope='module')
def ut():
    ut = uart_py()
    yield ut




@pytest.mark.stm32
def test_open_file(ut):
    logging.info("checking the file opened or not...")
    result = ut.file_open()
    assert result == True


@pytest.mark.stm32
def test_debug_mode(ut):
    logging.info("checking the working of debug mode...")
    assert ut.debug_mode() == True


@pytest.mark.stm32
def test_resume(ut):
    logging.info("checking the resume function...")
    assert ut.Resume() == True


@pytest.mark.stm32
def test_uart(ut):
    logging.info("printing uart output through com port using pyserial...")
    assert ut.connect_to_port() == "hello"


def test_close_app(ut):
    ut.app.kill()