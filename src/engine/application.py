from builtins import object

class Application(object):
    #Application Modules
    logger_module = None
    event_handler_module = None


    ##  Logger shortcuts
    core_logger=None
    CORE_CRIT=None
    CORE_ERROR=None
    CORE_WARN=None
    CORE_INFO=None
    CORE_DEBUG=None

    def initialize_logging_module(self, module):
        self.logger_module = module()
        self.core_logger=self.logger_module.get_corelogger()
        clientlog=self.logger_module.get_clientlogger()
        self.CORE_CRIT, self.CORE_ERROR, self.CORE_WARN, self.CORE_INFO, self.CORE_DEBUG = (self.core_logger.critical,
                                                                                            self.core_logger.error,
                                                                                            self.core_logger.warning,
                                                                                            self.core_logger.info,
                                                                                            self.core_logger.debug)
        self.CORE_WARN("Initialized Logger!")
        clientlog.info('Initialized Logger!')

    def initialize(self, logging_module=None):
        if not logging_module:
            from .default_modules.log import Log
            logging_module=Log
        self.initialize_logging_module(logging_module)

    def run(self):
        while True:
            print('Ran!')
            break

    @classmethod
    def create_application(cls):
        from .default_modules import log
        app = cls()
        app.initialize()
        return app
