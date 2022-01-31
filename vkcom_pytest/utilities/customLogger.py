from loguru import logger


class LogGen:
    @staticmethod
    def loggen():
        logger.add(r"C:\Selenium\vkcom\vkcom_pytest\logs\logs.log", format="{time},{level},{message}", level="INFO",
                   rotation="10 KB", compression="zip", serialize=True)
        return logger

# import logging
#
#
# class LogGen:
#     @staticmethod
#     def loggen():
#         log_format = '%(asctime)s: %(levelname)s: %(message)s'
#         # logging.basicConfig(level=logging.INFO, filename='automation.log', format='%(asctime)s: %(levelname)s: %(message)s',
#         #                     datefmt='%m/%d/%Y %I:%M:%S %p')
#         logging.basicConfig(filename='automation.log',
#                             level=logging.INFO, format=log_format)
#         file_handler = logging.FileHandler("automation.log")
#         file_handler.setLevel(logging.WARNING)
#         file_handler.setFormatter(logging.Formatter(log_format))
#         stream_handler = logging.StreamHandler()
#         stream_handler.setLevel(logging.INFO)
#         stream_handler.setFormatter(logging.Formatter(log_format))
#
#         logger = logging.getLogger()
#         logger.addHandler(file_handler)
#         logger.addHandler(stream_handler)
#
#         return logger

# log_format = "%(asctime)s: %(levelname)s: %(message)s ,datefmt ='%m/%d/%Y %I:%M:%S %p"
#
#
# def get_file_handler():
#     file_handler = logging.FileHandler("x.log")
#     file_handler.setLevel(logging.WARNING)
#     file_handler.setFormatter(logging.Formatter(log_format))
#     return file_handler
#
#
# def get_stream_handler():
#     stream_handler = logging.StreamHandler()
#     stream_handler.setLevel(logging.INFO)
#     stream_handler.setFormatter(logging.Formatter(log_format))
#     return stream_handler
#
#
# def get_logger():
#     logger = logging.getLogger()
#     logger.setLevel(logging.INFO)
#     logger.addHandler(get_file_handler())
#     logger.addHandler(get_stream_handler())
#     return logger
