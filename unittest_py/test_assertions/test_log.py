import logging
import unittest

# Set up logger
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

def log_messages():
    logger.debug("Debug message")
    logger.info("Info message")

class TestLogging(unittest.TestCase):
    def test_logging(self):
        with self.assertLogs(logger, level='DEBUG') as cm:
            log_messages()
        # Check if the "Debug message" is in the logs
        self.assertIn('Debug message', cm.output[0])  # cm.output is a list, first entry has the debug message

    def test_no_logs(self):
        with self.assertLogs(logger, level='DEBUG') as cm:
            logger.info("This is an info log")
        # No debug level logs should be present
        self.assertNotIn('Debug message', cm.output)

if __name__ == '__main__':
    unittest.main(verbosity=2)

