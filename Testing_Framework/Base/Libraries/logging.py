import logging


class logger:
    def __init__(self, file_path):
        self.logger = logging.getLogger(__name__)
        self.fh = logging.FileHandler(file_path, mode="a")
        self.frmt = logging.Formatter("%(asctime)s : %(name)s : %(levelname)s : %(message)s")
        self.fh.setFormatter(self.frmt)
        self.logger.addHandler(self.fh)
        self.logger.setLevel(logging.INFO)

