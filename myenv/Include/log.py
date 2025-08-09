import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%s'
    handlers=[
        logging.FileHandler('app.log')
        logging.StreamHandler()
    ]
)
loger=logging.getLogger('Arithmaticapp')
def add(a,b):
    logging.DEBUG("the addd is added to the logging")
    result=a+b
    logging.DEBUG('The add is complited')
add(2,3)
