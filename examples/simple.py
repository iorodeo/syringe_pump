import time
from syringe_pump import SyringePump

dev = SyringePump('/dev/ttyUSB1')
dev.debug = False 
dev.setDiameter(1.0)
dev.setRate(5.0,'NS')
dev.setAccumUnits('UL')
dev.clearVolumeAccum()
dev.setDirection('INF')
infuse, withdraw = dev.getVolumeAccum()
print('infuse: {0} (nl), withdraw: {1} (nl)'.format(infuse,withdraw))
dev.run()
time.sleep(3)
dev.setDirection('WDR')
time.sleep(3)
infuse, withdraw = dev.getVolumeAccum()
print('infuse: {0} (nl), withdraw: {1} (nl)'.format(infuse,withdraw))
dev.stop()
