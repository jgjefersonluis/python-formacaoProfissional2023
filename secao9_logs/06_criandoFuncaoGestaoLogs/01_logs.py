def custom_logger(level, message):
    import logging
    logger = logging.getLogger(__name__)
    if not (len(logger.handlers)):
        logging.basicConfig(level-logging.INFO)
        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler("file.log")
        format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        c_handler.setFormatter(format)
        f_handler.setFormatter(format)
        logger.addHandler(c_handler)
        logger.addHandler(f_handler)

    if level == 'debug':
        logger.debug(message)
    elif level == 'info':
        logger.info(message)
    elif level == 'warning':
        logger.warnig(message)
    elif level == 'error':
        logger.error(message)
    else:
        logger.critical(message)

custom_logger("warning", "Atenção, parametro errado!")
