import random

def s(x):
    if(x > 0):
        return x
    else:
        return 0

def establish_weights(network):
    weights = []
    for i in range(len(network)-1):
        w2 = []
        for j in range(network[i]):
            w3 = []
            if i != len(network) - 2:
                for k in range(network[i + 1] - 1):
                    w3.append(random.uniform(-2,2))
            else:
                for k in range(network[i + 1]):
                    w3.append(random.uniform(-2,2))
            w2.append(w3)
        weights.append(w2)
    return weights

def next_layer(input_layer, weights, network, layer_index):
    output = []
    for i in range(network[layer_index + 1] - 1):
        sum = 0
        for j in range(network[layer_index]):
            sum += input_layer[j] * weights[layer_index][j][i]
        output.append(s(sum))
    if layer_index != len(network) - 2:
        output.append(1)
    else:
        sum = 0
        for j in range(network[layer_index]):
            sum += input_layer[j] * weights[layer_index][j][network[layer_index + 1] - 1]
        output.append(s(sum))
    return output

network = [3, 6, 6, 6, 6, 1]
weights = establish_weights(network)
input_layer = [1, 1, 1]
layer_index = 0
print(input_layer)
for i in range(len(network) - 1):
    input_layer = next_layer(input_layer, weights, network, i)
    print(input_layer)
