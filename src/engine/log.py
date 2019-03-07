import logging
import pygogo as gogo

class Log():
    corelogger=None
    clientlogger=None

    def __init__(self):
        log_format = '[%(asctime)s] [%(levelname)s] - %(name)s: %(message)s'
        formatter =logging.Formatter(log_format)
        self.corelogger=gogo.Gogo('core',
                                    low_hdlr=gogo.handlers.file_hdlr('core.log'),
                                    low_formatter=formatter,
                                    high_level='info',
                                    high_formatter=formatter).logger
        self.clientlogger=gogo.Gogo('client',
                                    low_hdlr=gogo.handlers.file_hdlr('client.log'),
                                    low_formatter=formatter,
                                    high_level='info',
                                    high_formatter=formatter).logger
