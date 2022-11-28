

from EAM.config.config import config  #存放日志的文件路径，放在config
from loguru import logger


logger.add(config.log,encoding='utf-8')  #使用add，添加到文件里

