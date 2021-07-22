import configparser
import os

CONST_ROOT_DIR = os.path.dirname(os.path.abspath('../crawlers'))


def getPro(filename):
    cf = configparser.ConfigParser()
    return cf.read(CONST_ROOT_DIR + '/'+'filename'+'.ini')
