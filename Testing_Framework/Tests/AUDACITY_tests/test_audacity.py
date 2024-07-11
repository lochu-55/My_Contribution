from Base.Libraries.audacity import Audacity
from Base.Elements.Audacity_elements import Inputs
import pytest
from Base.Libraries.logging import logger


IN = Inputs()
obj = Audacity()
log = logger(IN.LOG_PATH)

@pytest.mark.audio
def test_open():
    log.logger.info("launching audacity")
    obj.Lauch_App(IN.APP)
    log.logger.info("opening the audio file")
    result = obj.Open(IN.OPEN_FILE_NAME)
    assert result == True
    obj.close_App()

@pytest.mark.audio

def test_play():
    log.logger.info("launching audacity")
    obj.Lauch_App(IN.APP)
    log.logger.info("opening the audio file")
    result = obj.Open(IN.OPEN_FILE_NAME)
    log.logger.info("playing the audio file")
    obj.play(IN.PLAY_TIME_IN_SEC)
    obj.close_App()

@pytest.mark.audio

def test_RMS():
    log.logger.info("launching audacity")
    obj.Lauch_App(IN.APP)
    log.logger.info("opening the audio file")
    result = obj.Open(IN.OPEN_FILE_NAME)
    log.logger.info("selecting the audio")
    obj.Select_entire_audio()
    log.logger.info("calculating the rms values")
    obj.Calculate_RMS(IN.FILE_TO_SAVE_RMS+r"/rms_value.png")
    obj.close_App()

@pytest.mark.audio

def test_Amplify():
    log.logger.info("launching audacity")
    obj.Lauch_App(IN.APP)
    log.logger.info("opening the audio file")
    result = obj.Open(IN.OPEN_FILE_NAME)
    log.logger.info("selecting the audio")
    obj.Select_entire_audio()
    log.logger.info("amplifying the audio")
    obj.Amplify(IN.AMPLIFY_VALUE)
    obj.close_App()

@pytest.mark.audio

def test_plot_spectrum():
    log.logger.info("launching audacity")
    obj.Lauch_App(IN.APP)
    log.logger.info("opening the audio file")
    result = obj.Open(IN.OPEN_FILE_NAME)
    log.logger.info("exporting plot analysis values")
    obj.plot(IN.FILE_PATH+r"\plotAnalysis.txt")
    obj.close_App()

@pytest.mark.audio

def test_generate_noise():
    log.logger.info("launching audacity")
    obj.Lauch_App(IN.APP)
    log.logger.info("generating the noise")
    obj.generate_noise()
    obj.close_App()

@pytest.mark.audio

def test_generate_silence():
    log.logger.info("launching audacity")
    obj.Lauch_App(IN.APP)
    log.logger.info("generating the silence")
    obj.generate_silence()
    obj.close_App()

@pytest.mark.audio

def test_select():
    log.logger.info("launching audacity")
    obj.Lauch_App(IN.APP)
    log.logger.info("opening the audio file")
    result = obj.Open(IN.OPEN_FILE_NAME)
    log.logger.info("selecting audio within specific period")
    obj.select(IN.START_TIME_TO_SELECT, IN.END_TIME_TO_SELECT)
    obj.noise_reduction()
    obj.close_App()

@pytest.mark.audio

def test_export_mp3():
    log.logger.info("launching audacity")
    obj.Lauch_App(IN.APP)
    log.logger.info("opening the audio file")
    result = obj.Open(IN.OPEN_FILE_NAME)
    log.logger.info("exporting the audio as mp3")
    obj.export_as_mp3()
    obj.close_App()

@pytest.mark.audio

def test_export_wav():
    log.logger.info("launching audacity")
    obj.Lauch_App(IN.APP)
    log.logger.info("opening the audio file")
    result = obj.Open(IN.OPEN_FILE_NAME)
    log.logger.info("exporting the audio as wav")
    obj.export_as_wav()
    obj.close_App()

@pytest.mark.audio

def test_export_flac():
    log.logger.info("launching audacity")
    obj.Lauch_App(IN.APP)
    log.logger.info("opening the audio file")
    result = obj.Open(IN.OPEN_FILE_NAME)
    log.logger.info("exporting the audio as flac")
    obj.export_as_flac()
    obj.close_App()

@pytest.mark.audio

def test_save_as():
    log.logger.info("launching audacity")
    obj.Lauch_App(IN.APP)
    log.logger.info("opening the audio file")
    result = obj.Open(IN.OPEN_FILE_NAME)
    log.logger.info("saving the audio file")
    obj.save_project_as(IN.SAVE_PROJECT)
    obj.close_App()
