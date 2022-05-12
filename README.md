# Quantitative-Microplankton-Tracker
[![arXiv](https://img.shields.io/badge/arXiv-2202.09046-b31b1b.svg)](https://arxiv.org/abs/2202.09046)

By Harshith Bachimanchi, Benjamin Midtvedt, Daniel Midtvedt, Erik Selander, and Giovanni Volpe.

The quantitiative microplankton tracker is a deep-learning based framework to predict dry masses and three-dimensional positions of microplankton from experimental holographic images. 

This repository contains source code and data for the arXiv preprint, [Microplankton life histories revealed by holographic microscopy and deep learning](https://arxiv.org/abs/2202.09046)

<p align="center">
  <img width="400" src=https://raw.githubusercontent.com/softmatterlab/Quantitative-Microplankton-Tracker/main/assets/setup.png>
</p>

## Description
The quantitative microplankton tracker uses two neural network in sequence to predict the dry masses and 3D positions of the microplanktons in holographic images. The first neural network, **Regression U-Net (RU-Net)**, segments single plankton holograms from a large field-of-view holographic image and predicts the dry masses and vertical positions. The second neural network, **Weighted Average Convolutional Neural network (WAC-Net)**, is then applied to the cropped image sequences of planktons to refine the plankton dry masses and vertical positions predicted by **RU-Net**.


## Usage
### Training-tutorials
We provide tutorials to train the neural networks, **RU-Net**, and, **WAC-Net**, from scratch in [training-tutorials](https://github.com/softmatterlab/Quantitative-Microplankton-Tracker/tree/main/training-tutorials).

1. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/softmatterlab/Quantitative-Microplankton-Tracker/blob/main/training-tutorials/1-training_RUNet.ipynb) [1-training_RUNet.ipynb](https://github.com/softmatterlab/Quantitative-Microplankton-Tracker/blob/main/training-tutorials/1-training_RUNet.ipynb) demonstrates the training process of **RU-Net**.

2. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/softmatterlab/Quantitative-Microplankton-Tracker/blob/main/training-tutorials/2-training_WACNet_drymass.ipynb) [2-training_WACNet_drymass.ipynb](https://github.com/softmatterlab/Quantitative-Microplankton-Tracker/blob/main/training-tutorials/2-training_WACNet_drymass.ipynb) demonstrates the training process of **WAC-Net** to predict plankton dry masses.

3. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/softmatterlab/Quantitative-Microplankton-Tracker/blob/main/training-tutorials/3-training_WACNet_z_distance.ipynb) [3-training_WACNet_z_distance.ipynb](https://github.com/softmatterlab/Quantitative-Microplankton-Tracker/blob/main/training-tutorials/3-training_WACNet_z_distance.ipynb) demonstrates the training process of **WAC-Net** to predict plankton vertical positions.

### Usage examples
We also provide additional examples in [examples](https://github.com/softmatterlab/Quantitative-Microplankton-Tracker/tree/main/examples) on how to apply pre-trained neural networks on experimental holographic images. PDF versions of examples are included for quick viewing.

1. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/softmatterlab/Quantitative-Microplankton-Tracker/blob/main/examples/1-example_RUNet.ipynb) [1-example_RUNet.ipynb](https://github.com/softmatterlab/Quantitative-Microplankton-Tracker/blob/main/examples/1-example_RUNet.ipynb) demonstrates how to use **RU-Net** on experimental holographic. The notebook also generates **figure 1** and **figure 2** of the paper.

2. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/softmatterlab/Quantitative-Microplankton-Tracker/blob/main/examples/2-example_WACNet.ipynb) [2-example_WACNet.ipynb](https://github.com/softmatterlab/Quantitative-Microplankton-Tracker/blob/main/examples/2-example_WACNet.ipynb) demonstrates how to use **WAC-Net** on cropped image sequences of planktons to obtain a refined dry mass value. The notebook also generates **figure 3** and **figure 4** in the paper.

3. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/softmatterlab/Quantitative-Microplankton-Tracker/blob/main/examples/3-example_Analysis.ipynb) [3-example_Analysis.ipynb](https://github.com/softmatterlab/Quantitative-Microplankton-Tracker/blob/main/examples/3-example_Analysis.ipynb) demonstrates the complete analysis pipeline, i.e., using **RU-Net** and **WAC-Net** in sequence.


## Citation
If you use this code for your research, please cite our paper:

<https://arxiv.org/abs/2202.09046>

```
Harshith Bachimanchi, Benjamin Midtvedt, Daniel Midtvedt, Erik Selander, and Giovanni Volpe.
"Microplankton life histories revealed by holographic microscopy and deep learning"
arXiv:2202.09046 (2022).
```

See also [DeepTrack2.1](https://github.com/softmatterlab/DeepTrack-2.0/tree/master):

```
Benjamin Midtvedt, Saga Helgadottir, Aykut Argun, Jesús Pineda, Daniel Midtvedt, Giovanni Volpe.
"Quantitative Digital Microscopy with Deep Learning."
Applied Physics Reviews 8 (2021), 011310.
https://doi.org/10.1063/5.0034891
```


## Funding
This work was partly supported by the H2020 European Research Council (ERC) Starting Grant ComplexSwimmers (Grant No. 677511), the Horizon Europe ERC Consolidator Grant MAPEI (Grant No. 101001267), the Knut and Alice Wallenberg Foundation (Grant No. 2019.0079), and the Swedish Research Council (VR, Grant No. 2019-05238).