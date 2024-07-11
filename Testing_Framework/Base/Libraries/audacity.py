from pywinauto.application import Application
from Base.Elements.Audacity_elements import Inputs
IN = Inputs()

import time


from PIL import Image


class Audacity:
    def Lauch_App(self,Application_name):
        # Launch Application
        self.app = Application(backend="uia").start(Application_name)
        # Wait for Audacity to fully load (adjust the delay time as needed)
        time.sleep(10)
        self.audacity_window = self.app.window(title='Audacity')
        self.audacity = self.app.top_window()
        # sometimes crash window occurs when you dont save the projects
        # if self.audacity_window.exists():
        #     print("\nAudacity opened Successfully\n")

        crash_window = self.audacity_window.child_window(title="Automatic Crash Recovery")
        if crash_window.exists():
            #print("crash recovery exists")
            crash_window.Skip.click()
            #crash_window.DiscardSelected.click()
            #time.sleep(2)
            #self.audacity_window.Yes.click()

    def close_App(self):
        self.app.kill()

    def Open(self, file_name_path):
        try:
            self.audacity_window.menu_select("File->Open")
            time.sleep(3)
            open_window = self.audacity_window.child_window(title="Select one or more files", control_type="Window")
            # open_window = self.app.Selectoneormorefiles
            open_window.type_keys(file_name_path + "{ENTER}")  # pass the filename to open
            time.sleep(5)
            self.file_open = self.app.window(title=IN.FILE_NAME)

            if self.file_open.exists():
                #print("file opened successfully")
                return True
            else:
                #print("file not opened")
                return False
        except Exception as err:
            print(err)

    def play(self, time_in_seconds):
        try:
            time.sleep(2)
            self.file_open.type_keys("+{SPACE}")
            time.sleep(int(time_in_seconds))# Here pass value that represents how many seconds you want to play the Audio
            self.file_open.type_keys("+{SPACE}")
            time.sleep(2)
        except Exception as err:
            print(err)

    def Select_entire_audio(self):
        self.file_open.type_keys("^a")

    def Calculate_RMS(self,file_name):
        try:
            time.sleep(5)
            self.file_open.menu_select("Analyze->Measure RMS ")
            time.sleep(5)
            ss = self.file_open.capture_as_image() #function to take screenshot
            ss.save(file_name)
            ss.show()
            self.file_open.Ok.click()
        except Exception as err:
            print(err)

    def Amplify(self,amplify_value):
        try:
            time.sleep(10)
            self.file_open.menu_select("Effects->Amplify...")
            amplify_dialog = self.audacity.child_window(title="Amplify")
            time.sleep(5)
            amplify_dialog.type_keys(amplify_value)
            if amplify_dialog.Checkbox.is_enabled():
                print('enabled')
            else:
                amplify_dialog.Checkbox.click()
            amplify_dialog.Apply.click()
        except Exception as err:
            print(err)


    def export_as_wav(self):
        try:
            self.file_open.menu_select("File->Export Audio")
            export_dialog = self.file_open.child_window(title="Export Audio", control_type="Window")
            self.clear(export_dialog.Edit2)
            export_dialog.Edit2.type_keys(IN.FILE_PATH)
            combo_box = self.file_open.child_window(title="Format:", auto_id="6000", control_type="ComboBox")
            combo_box.select("WAV (Microsoft)")
            export_dialog.Export.click()
            time.sleep(2)
        except Exception as err:
            print(err)

    def export_as_mp3(self):
        try:
            self.file_open.menu_select("File->Export Audio")
            export_dialog = self.file_open.child_window(title="Export Audio",control_type="Window")
            self.clear(export_dialog.Edit2)
            export_dialog.Edit2.type_keys(IN.FILE_PATH)
            combo_box = self.file_open.child_window(title="Format:", auto_id="6000", control_type="ComboBox")
            combo_box.select("MP3 Files")
            export_dialog.Export.click()
            time.sleep(2)
        except Exception as err:
            print(err)

    def export_as_flac(self):
        try:
            self.file_open.menu_select("File->Export Audio")
            export_dialog = self.file_open.child_window(title="Export Audio",control_type="Window")
            self.clear(export_dialog.Edit2)
            export_dialog.Edit2.type_keys(IN.FILE_PATH)
            combo_box = self.file_open.child_window(title="Format:", auto_id="6000", control_type="ComboBox")
            combo_box.select("FLAC Files")
            export_dialog.Export.click()
            time.sleep(2)
        except Exception as err:
            print(err)

    def save_project_as(self,file_name):
        try:
            time.sleep(2)
            self.file_open.type_keys("^s")
            save_as_dialog = self.file_open.child_window(title="Save Project 'jyo' As...", control_type="Window")
            # if save_as_dialog:
            #     print("yes")
            # else:
            #     print("No")
            self.file_open.child_window(title="File name:", auto_id="1148", control_type="Edit").type_keys(file_name)
            self.file_open.child_window(title="Save", auto_id="1", control_type="Button").click()
            overwrite_window = self.file_open.child_window(title="Overwrite Project Warning")
            time.sleep(2)

            class MyException(Exception):
                pass

            if overwrite_window:
                print("project exists give another name")
                time.sleep(2)
                overwrite_window.No.click()
                time.sleep(5)
                save_as_dialog.close()
                raise MyException("Project exists give another name ")

            else:
                print("Project Saved Successfully")
        except Exception as err:
            print(err)

    def plot(self,file_name):
        try:
            self.file_open.type_keys("^a")
            time.sleep(3)
            self.file_open.menu_select("Analyze->Plot Spectrum")
            time.sleep(5)
            plot_window = self.file_open.child_window(title="Frequency Analysis")
            ss = plot_window.capture_as_image()
            ss.save(IN.FILE_TO_SAVE_RMS+r"\Plotanalysis.png")
            plot_window.Export.click()
            export_window = self.file_open.child_window(title="Export Spectral Data As", control_type="Window")
            self.file_open.child_window(title="File name:", auto_id="1148", control_type="Edit").type_keys("{BACKSPACE}")
            self.file_open.child_window(title="File name:", auto_id="1148", control_type="Edit").type_keys(file_name)
            self.file_open.child_window(title="Save", auto_id="1", control_type="Button").click()
            plot_window.close()
        except Exception as err:
            print(err)

    def generate_noise(self):

        try:
            self.audacity_window.menu_select("Generate->Noise")
            noise_dialog = self.audacity_window.child_window(title="Noise", control_type="Window")
            time.sleep(5)
            self.audacity_window.child_window(title="Duration 00 h 00 m 00.000 s", auto_id="-31891",control_type="Text")
            noise_dialog.type_keys("{UP 1}")
            time.sleep(2)
            noise_dialog.Generate.click()
        except Exception as err:
            print(err)

    def generate_silence(self):
        try:
            self.audacity_window.menu_select("Generate->Silence")
            time.sleep(5)
            silence_dialog = self.audacity_window.child_window(title="Silence", control_type="Window")
            duration_text_control = self.audacity_window.child_window(title="Duration 00 h 00 m 00.000 s", auto_id="-31893",
                                                                  control_type="Text")
            time.sleep(3)
            duration_text_control.type_keys("{UP 3}")
            time.sleep(2)
            silence_dialog.Generate.click()
        except Exception as err:
            print(err)

    def clear(self, op):
        op.type_keys("^a")
        op.type_keys("{DELETE}")
        op.type_keys("{RIGHT}")

    def select(self,start_time,end_time): #enter time in seconds
        try:
            time.sleep(2)
            self.file_open.menu_select("Extra-> ScriptablesI")
            # self.file_open.child_window(title="Select Time...").click_input()
            self.audacity.child_window(title="Select Time...", auto_id="17340",control_type="MenuItem").click_input()
            self.clear(self.file_open.Edit1)
            self.file_open.Edit1.type_keys(start_time)
            time.sleep(2)
            self.clear(self.file_open.Edit2)
            self.file_open.Edit2.type_keys(end_time)
            time.sleep(2)
            self.audacity.Ok.click_input()
        except Exception as err:
            print(err)

    def noise_reduction(self):
        try:
            self.file_open.menu_select("Effect->Noise Reduction...")
            noise_dialog = self.audacity.child_window(title="Noise Reduction", control_type="Window")
            self.audacity.child_window(title="Get Noise Profile", auto_id="10001", control_type="Button").click_input()
            self.audacity.menu_select("Effect->Noise Reduction...")
            self.clear(noise_dialog.Edit1)
            time.sleep(3)
            noise_dialog.Edit1.type_keys("15")
            noise_dialog.Ok.click()
        except Exception as err:
            print(err)
