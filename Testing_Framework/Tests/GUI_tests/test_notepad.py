from Base.Libraries.notepad import Notepad
from Base.Elements.GUI_elements import Elements
import sys
import pytest
from Base.Libraries.logging import logger

ele = Elements()
obj = Notepad()
log = logger(ele.LOG_PATH2)

sys.path.append(r'C:\Users\vlab\Desktop\pywinautoJyo')

@pytest.mark.pywinauto
def test_open_notepad():
    log.logger.info("checking whether {APP} is opening ")
    result = obj.open_notepad()
    assert result == True
    obj.close_notepad()


@pytest.mark.pywinauto
def test_edit():
    log.logger.info("opening notepad")
    obj.open_notepad()
    log.logger.info("Editing text in notepad")
    result = obj.Edit_text(ele.TEXT)
    log.logger.info("checking that text edited correctly")
    assert result == ele.TEXT
    log.logger.info("Closing notepad")
    obj.close_notepad()


@pytest.mark.pywinauto
def test_find():
    log.logger.info("opening notepad")
    obj.open_notepad()
    log.logger.info("Editing text in notepad")
    obj.Edit_text(ele.TEXT)

    log.logger.info("Finding text in notepad")
    result = obj.find(ele.FIND_TEXT)
    assert result == True
    log.logger.info("Closing notepad")
    obj.close_notepad()


@pytest.mark.pywinauto
def test_replace():
    log.logger.info("opening notepad")
    obj.open_notepad()
    log.logger.info("Editing text in notepad")
    obj.Edit_text(ele.TEXT)
    log.logger.info("Replacing text in notepad")
    result = obj.find_replace()
    assert result == True
    log.logger.info("Closing notepad")
    obj.close_notepad()


@pytest.mark.pywinauto
def test_change_font():
    log.logger.info("opening notepad")
    obj.open_notepad()
    log.logger.info("Editing text in notepad")
    obj.Edit_text(ele.TEXT)
    log.logger.info("Changing Font,Font Style,Font Size for text")
    obj.change_font()
    log.logger.info("Closing notepad")
    obj.close_notepad()


@pytest.mark.pywinauto
def test_pagesetup():
    log.logger.info("opening notepad")
    obj.open_notepad()
    log.logger.info("Editing text in notepad")
    obj.Edit_text(ele.TEXT)
    log.logger.info("changing page setup settings")
    obj.pagesetup()
    log.logger.info("Closing notepad")
    obj.close_notepad()


@pytest.mark.pywinauto
def test_time():
    log.logger.info("opening notepad")
    obj.open_notepad()
    log.logger.info("printing date and time in file")
    obj.time()
    log.logger.info("Closing notepad")
    obj.close_notepad()


@pytest.mark.pywinauto
def test_print():
    log.logger.info("opening notepad")
    obj.open_notepad()
    log.logger.info("Editing text in notepad")
    obj.Edit_text(ele.TEXT)
    log.logger.info("printing file")
    obj.print()
    log.logger.info("Closing notepad")
    obj.close_notepad()


@pytest.mark.pywinauto
def test_select_all():
    log.logger.info("opening notepad")
    obj.open_notepad()
    log.logger.info("Editing text in notepad")
    obj.Edit_text(ele.TEXT)
    log.logger.info("selecting all the text and deleting and doing undo in notepad")
    obj.select_all()
    log.logger.info("Closing notepad")
    obj.close_notepad()


@pytest.mark.pywinauto
def test_zoom():
    log.logger.info("opening notepad")
    obj.open_notepad()
    log.logger.info("Editing text in notepad")
    obj.Edit_text(ele.TEXT)
    log.logger.info("zooming the text")
    obj.view()
    log.logger.info("Closing notepad")
    obj.close_notepad()


@pytest.mark.pywinauto
def test_about():
    log.logger.info("opening notepad")
    obj.open_notepad()
    log.logger.info("printing about notepad")
    obj.about()
    log.logger.info("Closing notepad")
    obj.close_notepad()


@pytest.mark.pywinauto
def test_save():
    log.logger.info("opening notepad")
    obj.open_notepad()
    log.logger.info("Editing text in notepad")
    obj.Edit_text(ele.TEXT)
    log.logger.info("checking that the file saved successfully")
    result = obj.Save_File(ele.FILE_NAME_TO_SAVE)
    assert result == ele.FILE_NAME_TO_SAVE + " - Notepad", "FILE NOT SAVED"


@pytest.mark.pywinauto
def test_open():
    log.logger.info("opening notepad")
    obj.open_notepad()
    log.logger.info("Opening existing file notepad")
    result = obj.open_file(ele.FILE_NAME_TO_OPEN)
    assert result == True, "FILE NOT FOUND ERROR"
    # assert result == "b1 - Notepad"
    log.logger.info("Closing notepad")
    obj.close_notepad()
