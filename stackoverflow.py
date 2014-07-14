from datetime import date,datetime
import time

d = datetime.fromtimestamp(time.time())
print d
print d.strftime("%d-%b-%Y %H:%M:%S")