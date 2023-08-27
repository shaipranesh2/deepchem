import os
import pytest
import deepchem as dc
import pandas as pd


@pytest.fixture
def grover_graph_attributes():
    from deepchem.feat.graph_data import BatchGraphData
    from deepchem.utils.grover import extract_grover_attributes
    smiles = ['CC', 'CCC', 'CC(=O)C']

    fg = dc.feat.CircularFingerprint()
    featurizer = dc.feat.GroverFeaturizer(features_generator=fg)

    graphs = featurizer.featurize(smiles)
    batched_graph = BatchGraphData(graphs)
    attributes = extract_grover_attributes(batched_graph)
    return attributes


@pytest.fixture
def smiles_regression_dataset(tmpdir):
    smiles = [
        "CCN(CCSC)C(=O)N[C@@](C)(CC)C(F)(F)F",
        "CC1(C)CN(C(=O)Nc2cc3ccccc3nn2)C[C@@]2(CCOC2)O1"
    ]
    labels = [3.112, 2.432]
    df = pd.DataFrame(list(zip(smiles, labels)), columns=["smiles", "task1"])
    filepath = os.path.join(tmpdir, 'smiles.csv')
    df.to_csv(filepath)

    loader = dc.data.CSVLoader(["task1"],
                               feature_field="smiles",
                               featurizer=dc.feat.DummyFeaturizer())
    dataset = loader.create_dataset(filepath)
    return dataset


@pytest.fixture
def smiles_multitask_regression_dataset():
    cwd = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(cwd,
                              '../../tests/assets/multitask_regression.csv')

    loader = dc.data.CSVLoader(tasks=['task0', 'task1'],
                               feature_field='smiles',
                               featurizer=dc.feat.DummyFeaturizer())
    dataset = loader.create_dataset(input_file)
    return dataset
