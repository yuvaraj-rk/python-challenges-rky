import logging

# Configure logging to write to a file
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('This is a debug message.')
logging.info('This is an info message.')
logging.warning('This is a warning message.')
