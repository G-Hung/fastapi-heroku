import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(asctime)s [%(filename)s:%(funcName)s:%(lineno)d]\n%(message)s\n",
)
logger = logging.getLogger()
