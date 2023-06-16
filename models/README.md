# Models

## `trained_model.pt`
A neural network with the following structure:
```
NeuralNetwork(
  (flatten): Flatten(start_dim=1, end_dim=-1)
  (linear_relu_stack): Sequential(
    (0): Linear(in_features=784, out_features=512, bias=True)
    (1): ReLU()
    (2): Linear(in_features=512, out_features=512, bias=True)
    (3): ReLU()
    (4): Linear(in_features=512, out_features=10, bias=True)
  )
)
```
Training parameters:
- Learning rate: 1e-3
- Batch size: 64
- Epochs: 5
- Loss: cross-entropy loss

Test performance:
- Accuracy: 98.2 %
