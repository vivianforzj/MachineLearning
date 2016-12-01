
## Book

Data Science from Scratch First Principles with Python

## Recordings

### Chapter 11. Machine Learning

#### Overfitting and underfitting

给出如下图：

![overfitting and underfitting](./overfitting_underfitting.png)

- Underfitting：如图中degree 0表示即使是预测训练出这个模型的训练集，结果也会很差。此时模型具有high bias，可以通过加入更多的feature来训练出更好的模型。
- Overfitting：如图degree 9表示预测训练出这个模型的训练集，结果非常好，但是对于任何一个新的数据集，结果都非常差。此时模型具有high variance，可以通过减少feature来训练出更好的模型。

