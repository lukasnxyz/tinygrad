from helpers import tinytrange
import time

for i in (t := tinytrange(100)):
  time.sleep(0.02)
  t.set_description(f'iter {i}')