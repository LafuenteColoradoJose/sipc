import json

data = open('/home/pp/Escritorio/Proyectos/sipc/public/model/tfjs_model/group1-shard1of1.bin', 'rb').read()
import struct
floats = struct.unpack(f'<{len(data)//4}f', data)
print(floats[:10])
