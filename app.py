from SignLengueage.logger import logging
import sys
#logging.info("Welcome to the project")

from SignLengueage.exception import SignLanguage
try :
    a=7/'9'
except Exception as e:
    raise SignLanguage(e,sys) from e
