CRIT=None
ERROR=None
WARN=None
INFO=None
DEBUG=None



## Core Logger functions
CORE_CRIT=None
CORE_ERROR=None
CORE_WARN=None
CORE_INFO=None
CORE_DEBUG=None

def init_logger():
    from .log import Log
    log = Log()
    corelog=log.corelogger
    clientlog=log.clientlogger
    CORE_CRIT=corelog.critical
    CORE_ERROR=corelog.error
    CORE_WARN=corelog.warning
    CORE_INFO=corelog.info
    CORE_DEBUG=corelog.debug
    CRIT=clientlog.critical
    ERROR=clientlog.error
    WARN=clientlog.warning
    INFO=clientlog.info
    DEBUG=clientlog.debug
    CORE_WARN("Initialized Logger!")
    INFO('Initialized Logger!')


def run(app_class):
    from .application import Application
    init_logger()
    app = app_class.create_application()
    app.run()
