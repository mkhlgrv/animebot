from dotenv import load_dotenv
import os
load_dotenv()
import logging.handlers

# создаю логер
logger = logging.getLogger(__name__)
# os.environ.get("LOGFILE", ".log") - мы просто берем env переменную LOGFILE. с дефолтным значением .log
# добавлю хэндлер - для логгера это место куда он записывает логи.
# WatchedFileHandler - подключается к выбранному файлу и логи передает туда
# примеры еще: stdout 
handler = logging.handlers.WatchedFileHandler(
    os.environ.get("LOGFILE", ".log"))

logger.addHandler(handler)
# форматирование: что мы хотим видеть в сообщении логгера. мы хотим видеть время и само сообщение (ошибка, исключение)
# есть другие типы того, что можно вывести (либо можно задать extra = {"name":script_name, "prc":dt}
# logging.Formatter('%(asctime)s %(name)s: %(prc)f %(message)s', extra = extra)
formatter = logging.Formatter('%(asctime)s: %(message)s')
handler.setFormatter(formatter)
# атрибут LOGLEVEL - это уровень логирования
logger.setLevel(os.environ.get("LOGLEVEL", "INFO"))
logger = logging.LoggerAdapter(logger, extra=None)