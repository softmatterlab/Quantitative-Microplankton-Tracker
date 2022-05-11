# Quantitative-Microplankton-Tracker
[![arXiv](https://img.shields.io/badge/arXiv-2202.09046-b31b1b.svg)](https://arxiv.org/abs/2202.09046)

By Harshith Bachimanchi, Benjamin Midtvedt, Daniel Midtvedt, Erik Selander, and Giovanni Volpe.

Quantitiative microplankton tracker is a deep-learning based framework for predicting dry mass, and three-dimensional positions of microplankton species from experimental holographic images. 

The repository contains source code for the arXiv preprint, [Microplankton life histories revealed by holographic microscopy and deep learning](https://arxiv.org/abs/2202.09046)

<p align="center">
  <img width="400" src=https://raw.githubusercontent.com/softmatterlab/Quantitative-Microplankton-Tracker/main/assets/setup.png>
</p>

## Description
Quantitative microplankton tracker uses two neural network architectures (RU-Net and WAC-Net) in sequence to predict the dry mass, and 3D positions of the microplanktons. The first neural network, ```Regression U-Net (RU-Net)``` segments single plankton holograms from a large field-of-view holographic image , along with their dry mass and z-distance properties. The predictions are then refined by an additional neural network, ```Weighted average convolutional neural network (WAC-Net)``` applied to the cropped image sequences that detail individual plankton.


## Usage
### Training-tutorials
We provide tutorials to train the neural networks, RU-Net and WAC-Net from scratch in ```training-tutorials```.

1. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/softmatterlab/Quantitative-Microplankton-Tracker/blob/main/training-tutorials/1-training_RUNet.ipynb) [1-training_RUNet.ipynb](https://github.com/softmatterlab/Quantitative-Microplankton-Tracker/blob/main/training-tutorials/1-training_RUNet.ipynb) explains how to train RU-Net from scratch.

2. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/softmatterlab/Quantitative-Microplankton-Tracker/blob/main/training-tutorials/2-training_WACNet_drymass.ipynb) [2-training_WACNet_drymass.ipynb](https://github.com/softmatterlab/Quantitative-Microplankton-Tracker/blob/main/training-tutorials/2-training_WACNet_drymass.ipynb) demonstrates the training process of WAC-Net for dry mass predictions.

3. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/softmatterlab/Quantitative-Microplankton-Tracker/blob/main/training-tutorials/3-training_WACNet_z_distance.ipynb) [3-training_WACNet_z_distance.ipynb](https://github.com/softmatterlab/Quantitative-Microplankton-Tracker/blob/main/training-tutorials/3-training_WACNet_z_distance.ipynb) demonstrates the training process of WAC-Net for z-distance predictions.

### Usage examples
We also provide additional examples in ```examples``` on how to apply pre-trained neural networks on experimental holographic images.

1. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/softmatterlab/Quantitative-Microplankton-Tracker/blob/main/examples/1-example_RUNet.ipynb) [1-example_RUNet.ipynb](https://github.com/softmatterlab/Quantitative-Microplankton-Tracker/blob/main/examples/1-example_RUNet.ipynb) demonstrates how to use RU-Net on experimental holographic images to extract properties.

2. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/softmatterlab/Quantitative-Microplankton-Tracker/blob/main/examples/2-example_WACNet.ipynb) [2-example_WACNet.ipynb](https://github.com/softmatterlab/Quantitative-Microplankton-Tracker/blob/main/examples/2-example_WACNet.ipynb) demonstrates how to use WAC-Net on experimental crops of planktons to obtain a refined dry mass value.

3. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/softmatterlab/Quantitative-Microplankton-Tracker/blob/main/examples/3-example_Analysis.ipynb) [3-example_Analysis.ipynb](https://github.com/softmatterlab/Quantitative-Microplankton-Tracker/blob/main/examples/3-example_Analysis.ipynb) demonstrates the complete analysis pipeline, i.e, using RU-Net and WAC-Net in sequence.


## Citation
If you use this code for your research, please cite our paper:

```
Harshith Bachimanchi, Benjamin Midtvedt, Daniel Midtvedt, Erik Selander, and Giovanni Volpe.
"Microplankton life histories revealed by holographic microscopy and deep learning"
arXiv:2202.09046 (2022).
```

<https://arxiv.org/abs/2202.09046>


## Funding
This work was partly supported by the H2020 European Research Council (ERC) Starting Grant ComplexSwimmers (Grant No. 677511), the Horizon Europe ERC Consolidator Grant MAPEI (Grant No. 101001267), the Knut and Alice Wallenberg Foundation (Grant No. 2019.0079), and the Swedish Research Council (VR, Grant No. 2019-05238).