from loguru import logger


class LogGen:
    @staticmethod
    def loggen():
        logger.remove()
        logger.add(r"C:\Selenium\vkcom\vkcom_pytest\logs\logs.log", format="{time},{level},{message}", level="INFO",
                   rotation="10 KB", compression="zip", colorize=True
                   )
        return logger
