from time import sleep
from pywinauto.application import Application
from Base.Elements.GUI_elements import Elements

ele = Elements()


class Notepad:
    def open_notepad(self):
        try:
            self.app = Application(backend="uia").start(ele.APP)
        except:
            return False
        self.main_window = self.app.UntitledNotepad
        self.notepad_window = self.app.top_window()
        sleep(2)
        return True

    def close_notepad(self):
        self.app.kill()
        # close_button = self.notepad_window.child_window(title="Close", control_type="Button")
        # close_button.click_input()

    def Edit_text(self, text):
        file_content = None
        try:
            self.main_window.Edit.type_keys(text, with_spaces=True, with_newlines=True, pause=0.1)
            file_content = self.app.UntitledNotepad.Edit.get_value()
            e = file_content.capture_as_image()
            e.save("pic.png")
        except AssertionError:
            i = self.notepad_window.capture_as_image()
            i.save(ele.PATH + r"\edit1.png")
        except Exception as ex:
            print(ex)
            i = self.notepad_window.capture_as_image()
            i.save(ele.PATH + r"\edit2.png")
        return file_content

    def Save_File(self, filename):
        self.notepad_window.menu_select("File->Save As")
        # self.notepad_window.SaveAs.print_control_identifiers()
        save_as_dialog = self.notepad_window.child_window(title="Save As", control_type="Window")
        print("class name-----", save_as_dialog.class_name())
        save_as_dialog.type_keys(filename + "{ENTER}")
        sleep(2)
        confirm_save = self.notepad_window.child_window(title="Confirm Save As", control_type="Window")
        no_button = confirm_save.child_window(title="No", control_type="Button")

        if no_button.exists():
            print("Dialog type: Confirm Replace File - File already exists")
            print("file exists ,give another name.....")
            i = self.notepad_window.capture_as_image()
            i.save(ele.PATH + r"\save.png")
            confirm = self.notepad_window.child_window(title="Confirm Save As", control_type="Window")
            confirm.No.click_input()
            save_as_dialog.close()
            title = self.app.UntitledNotepad.window_text()
            print("title---", title)
            self.close_notepad()
            sleep(2)
            # self.app.UntitledNotepad.print_control_identifiers()
            dont_save = self.notepad_window.child_window(title="Don't Save", auto_id="CommandButton_7",
                                                         control_type="Button")
            dont_save.click()
            sleep(2)
            return title

        else:
            title = self.app.Notepad.window_text()
            print("title---", title)
            return title

    def open_file(self, filename):
        self.notepad_window.menu_select("File->Open")
        self.open_window = self.notepad_window.child_window(title="Open", control_type="Window")
        self.open_window.type_keys(filename + "{ENTER}")
        # print(self.app.UntitledNotepad.print_control_identifiers())
        self.open_window1 = self.notepad_window.child_window(title="Open", auto_id="1", control_type="Button")
        i = self.notepad_window.capture_as_image()
        i.save(ele.PATH + r"\open.png")
        sleep(2)
        if self.open_window1.exists():
            self.open_window1.close()
            self.close_notepad()
            return False
        else:
            return True
        # open_window.ComboBox2.select(1)
        # open_window.Open.click()
        # title = self.app.Notepad.window_text()
        # return title

    def change_font(self):
        self.main_window.menu_select("Format->Font")
        font_dialog = self.notepad_window.child_window(title="Font", control_type="Window")
        font_dialog.Edit.type_keys(ele.FONT, with_spaces=True)
        font_dialog.Edit2.type_keys(ele.FONT_STYLE)
        font_dialog.Edit3.type_keys(ele.FONT_SIZE)
        i = self.notepad_window.capture_as_image()
        i.save(ele.PATH + r"\font.png")
        font_dialog.Ok.click()
        sleep(2)

    def find(self, find_text):
        self.main_window.menu_select("Edit->Find")
        # find= self.app.Find
        find_dialog = self.notepad_window.child_window(title="Find", control_type="Window")
        find_dialog.Edit.type_keys(find_text)
        i = self.notepad_window.capture_as_image()
        i.save(ele.PATH + r"\find.png")
        checkbox1 = find_dialog.Checkbox1
        state = checkbox1.get_toggle_state()
        if state == 0:
            checkbox1.click()

        checkbox2 = find_dialog.Checkbox2
        state = checkbox2.get_toggle_state()
        if state == 0:
            checkbox1.click()

        radiobutton = find_dialog.RadioButton2
        radiobutton.click()
        find_dialog.FindNext.click()

        # self.app.UntitledNotepad.print_control_identifiers()
        self.notepad = self.notepad_window.child_window(title="Notepad", control_type="Window")
        if self.notepad.exists():
            self.notepad.close()
            find_dialog.close()
            self.close_notepad()
            return False
        else:
            find_dialog.close()
            self.close_notepad()
            return True

    def find_replace(self):
        self.notepad_window.menu_select("Edit->Replace")
        # self.notepad_window.print_control_identifiers()
        replace_dialog = self.notepad_window.child_window(title="Replace", control_type="Window")
        replace_dialog.Edit1.set_text("")
        sleep(1)
        replace_dialog.Edit1.type_keys(ele.FIND_TEXT_TO_REPLACE)
        sleep(1)
        replace_dialog.Edit2.set_text("")
        sleep(1)
        replace_dialog.Edit2.type_keys(ele.REPLACE_WITH)
        i = self.notepad_window.capture_as_image()
        i.save(ele.PATH + r"\replace.png")
        replace_dialog.ReplaceAll.click()
        sleep(3)
        self.notepad = self.notepad_window.child_window(title="Notepad", control_type="Window")
        if self.notepad.exists():
            self.notepad.close()
            replace_dialog.close()
            self.close_notepad()
            return False
        else:
            sleep(3)
            replace_dialog.close()
            self.close_notepad()
            return True

    def time(self):
        self.notepad_window.menu_select("Edit->Time/Date")
        i = self.notepad_window.capture_as_image()
        i.save(ele.PATH + r"\time.png")
        sleep(2)

    def select_all(self):
        self.notepad_window.menu_select("Edit->SelectAll")
        sleep(2)
        self.notepad_window.menu_select("Edit->Delete")
        i = self.notepad_window.capture_as_image()
        i.save(ele.PATH + r"\delete.png")
        sleep(2)
        self.notepad_window.menu_select("Edit->undo")
        sleep(2)

    def view(self):
        self.notepad_window.child_window(title="View", control_type="MenuItem").click_input()
        self.notepad_window.child_window(title="Zoom", control_type="MenuItem").click_input()
        # self.notepad_window.print_control_identifiers()
        self.notepad_window.child_window(title="Zoom In	Ctrl+Plus", auto_id="34",
                                         control_type="MenuItem").click_input()
        i = self.notepad_window.capture_as_image()
        i.save(ele.PATH + r"\zoomin.png")
        sleep(2)
        self.notepad_window.child_window(title="Zoom Out	Ctrl+Minus", auto_id="35", control_type="MenuItem")
        i = self.notepad_window.capture_as_image()
        i.save(ele.PATH + r"\zoomout.png")
        sleep(2)

    def about(self):
        self.notepad_window.menu_select("Help->About Notepad")
        sleep(1)
        # self.notepad_window.print_control_identifiers()
        self.notepad_window.child_window(title="About Notepad", control_type="Window").close()
        # self.app.UntitledNotepad.Ok.click_input()
        sleep(1)
        # self.notepad_window.menu_select("Help->View Help")
        # self.notepad_window.menu_select("Help->Send Feedback")

    def pagesetup(self):
        self.notepad_window.menu_select("File->PageSetup")
        # self.notepad_window.print_control_identifiers()
        pagesetup_window = self.notepad_window.child_window(title="Page Setup", control_type="Window")
        combo_box = pagesetup_window.ComboBox1
        combo_box.select("A4")
        sleep(1)
        radio_button = pagesetup_window.RadioButton2
        radio_button.click()
        sleep(1)
        pagesetup_window.Edit1.set_text("10")
        sleep(1)
        pagesetup_window.Edit2.set_text("15")
        sleep(1)
        pagesetup_window.Edit3.set_text("20")
        sleep(1)
        pagesetup_window.Edit4.set_text("25")
        pagesetup_window.Edit5.set_text("")
        sleep(1)
        pagesetup_window.Edit5.set_text("welcome")
        sleep(1)
        pagesetup_window.Edit6.set_text("")
        sleep(1)
        pagesetup_window.Edit6.set_text("By Sri Jyothsna")
        i = self.notepad_window.capture_as_image()
        i.save(ele.PATH + r"\pageset.png")
        sleep(1)
        pagesetup_window.Ok.click()

    def print(self):
        self.notepad_window.menu_select("File->Print")
        # self.notepad_window.print_control_identifiers()
        print_window = self.notepad_window.child_window(title="Print", control_type="Window")
        print_window.Edit5.set_text("3")
        i = self.notepad_window.capture_as_image()
        i.save(ele.PATH + r"\print.png")
        print_window.Print.click()
