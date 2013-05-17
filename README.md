EXAMPLE CODE:

import velopy
import sys
from time import sleep



apivelo = velopy.api('YOUR-API-KEY') # see https://developer.jcdecaux.com/#/home



while True:
	strApi  = apivelo.getCSVallstations()
	file = open(sys.argv[1],'a')
	file.write(strApi + '\n')
	sleep(30)
