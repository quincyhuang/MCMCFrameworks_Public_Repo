import os
import sys

os.rename(sys.argv[1], sys.argv[2])
print('renamed file <' + sys.argv[1] +'> to <' + sys.argv[2] +'>')