import logging
import pytest

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("test_log.log"),
                        logging.StreamHandler()
                    ])

log = logging.getLogger(__name__)

def test_add():
    pass
