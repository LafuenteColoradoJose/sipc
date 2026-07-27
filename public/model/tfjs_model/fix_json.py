import json

with open('model.json', 'r') as f:
    data = json.load(f)

# Modify layers to remove InputLayer and put batchInputShape on the first Dense layer
layers = data['modelTopology']['model_config']['config']['layers']

if layers[0]['class_name'] == 'InputLayer':
    input_layer = layers.pop(0)
    batch_input_shape = input_layer['config'].get('batchInputShape') or input_layer['config'].get('batch_shape')
    dtype = input_layer['config'].get('dtype')
    
    # Add to first Dense layer
    layers[0]['config']['batchInputShape'] = batch_input_shape
    layers[0]['config']['dtype'] = dtype

# Remove build_input_shape which confuses TFJS
if 'build_input_shape' in data['modelTopology']['model_config']['config']:
    del data['modelTopology']['model_config']['config']['build_input_shape']

with open('model.json', 'w') as f:
    json.dump(data, f)
print("model.json fixed successfully")
