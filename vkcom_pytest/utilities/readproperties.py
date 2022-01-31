from configparser import ConfigParser

config = ConfigParser()
config.read(r'C:\Selenium\vkcom\vkcom_pytest\configurations\config.ini')


class ReadConfig:
    @staticmethod
    def getURL():
        url = config['common info']['mainURL']
        return url

    @staticmethod
    def vk_login():
        vk_login = config['common info']['vk_login']
        return vk_login

    @staticmethod
    def vk_password():
        vk_password = config['common info']['vk_password']
        return vk_password
