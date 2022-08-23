Layers
======
Deep learning models are often said to be made up of "layers".
Intuitively, a "layer" is a function which transforms some
tensor into another tensor. DeepChem maintains an extensive
collection of layers which perform various useful scientific
transformations. For now, most layers are Keras only but over
time we expect this support to expand to other types of models
and layers.

Keras Layers
------------

.. autoclass:: deepchem.models.layers.InteratomicL2Distances
  :members:

.. autoclass:: deepchem.models.layers.GraphConv
  :members:

.. autoclass:: deepchem.models.layers.GraphPool
  :members:

.. autoclass:: deepchem.models.layers.GraphGather
  :members:

.. autoclass:: deepchem.models.layers.MolGANConvolutionLayer
  :members:

.. autoclass:: deepchem.models.layers.MolGANAggregationLayer
  :members:

.. autoclass:: deepchem.models.layers.MolGANMultiConvolutionLayer
  :members:

.. autoclass:: deepchem.models.layers.MolGANEncoderLayer
  :members:

.. autoclass:: deepchem.models.layers.LSTMStep
  :members:

.. autoclass:: deepchem.models.layers.AttnLSTMEmbedding
  :members:

.. autoclass:: deepchem.models.layers.IterRefLSTMEmbedding
  :members:

.. autoclass:: deepchem.models.layers.SwitchedDropout
  :members:

.. autoclass:: deepchem.models.layers.WeightedLinearCombo
  :members:

.. autoclass:: deepchem.models.layers.CombineMeanStd
  :members:

.. autoclass:: deepchem.models.layers.Stack
  :members:

.. autoclass:: deepchem.models.layers.VinaFreeEnergy
  :members:

.. autoclass:: deepchem.models.layers.NeighborList
  :members:

.. autoclass:: deepchem.models.layers.AtomicConvolution
  :members:

.. autoclass:: deepchem.models.layers.AlphaShareLayer
  :members:
  
.. autoclass:: deepchem.models.layers.SluiceLoss
  :members:
  
.. autoclass:: deepchem.models.layers.BetaShare
  :members:

.. autoclass:: deepchem.models.layers.ANIFeat
  :members:

.. autoclass:: deepchem.models.layers.GraphEmbedPoolLayer
  :members:

.. autoclass:: deepchem.models.layers.GraphCNN
  :members:

.. autoclass:: deepchem.models.layers.Highway
  :members:

.. autoclass:: deepchem.models.layers.WeaveLayer
  :members:

.. autoclass:: deepchem.models.layers.WeaveGather
  :members:

.. autoclass:: deepchem.models.layers.DTNNEmbedding
  :members:

.. autoclass:: deepchem.models.layers.DTNNStep
  :members:

.. autoclass:: deepchem.models.layers.DTNNGather
  :members:

.. autoclass:: deepchem.models.layers.DAGLayer
  :members:

.. autoclass:: deepchem.models.layers.DAGGather
  :members:

.. autoclass:: deepchem.models.layers.MessagePassing
  :members:

.. autoclass:: deepchem.models.layers.EdgeNetwork
  :members:

.. autoclass:: deepchem.models.layers.GatedRecurrentUnit
  :members:

.. autoclass:: deepchem.models.layers.SetGather
  :members:

Torch Layers
------------

.. autoclass:: deepchem.models.torch_models.layers.CNNModule
  :members:

.. autoclass:: deepchem.models.torch_models.layers.ScaleNorm
  :members:

.. autoclass:: deepchem.models.torch_models.layers.MATEncoderLayer
  :members:

.. autoclass:: deepchem.models.torch_models.layers.MultiHeadedMATAttention
  :members:

.. autoclass:: deepchem.models.torch_models.layers.SublayerConnection
  :members:

.. autoclass:: deepchem.models.torch_models.layers.PositionwiseFeedForward
  :members:

.. autoclass:: deepchem.models.torch_models.layers.MATEmbedding
  :members:

.. autoclass:: deepchem.models.torch_models.layers.MATGenerator
  :members:

.. autofunction:: deepchem.models.layers.cosine_dist

.. autoclass:: deepchem.models.torch_models.layers.GraphNetwork
  :members:

.. autoclass:: deepchem.models.torch_models.layers.Affine
  :members:

.. autoclass:: deepchem.models.torch_models.layers.DMPNNEncoderLayer
  :members:

Jax Layers
----------

.. autoclass:: deepchem.models.jax_models.layers.Linear
  :members:
