#https://www.geeksforgeeks.org/arecord-command-in-linux-with-examples/

import os 
import logging

logging.basicConfig(
    level = logging.DEBUG, 
    format = '%(message)s'
    )


logging.info('Comenzando grabacion')
os.system('arecord -d 10 -f U8 -r 8000 prueba.mp3')

logging.info('Grabacion finalizada, inicia reproduccion')
os.system('aplay prueba.mp3')
