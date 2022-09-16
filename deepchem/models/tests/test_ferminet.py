"""
Test for Ferminet Model.
"""

import pytest

try:
  import torch
  from deepchem.models.torch_models.ferminet import Ferminet
  from deepchem.models.torch_models.ferminet import FerminetModel
except ModuleNotFoundError:
  pass


@pytest.mark.torch
def test_prepare_input_stream():
  # test for the prepare_input_stream function of Ferminet class

  h2_molecule = [['H', [0, 0, 0]], ['H', [0, 0, 0.748]]]
  molecule = FerminetModel(h2_molecule, spin=0, charge=0, seed=0, batch_no=1)

  fermi = Ferminet(torch.Tensor([[0, 0, 0], [0, 0, 0.748]]),
                   spin=(molecule.up_spin, molecule.down_spin),
                   nuclear_charge=torch.from_numpy(molecule.charge),
                   inter_atom=torch.from_numpy(molecule.inter_atom))

  fermi.forward(torch.from_numpy(molecule.molecule.x))

  potential = fermi.calculate_potential()
  assert torch.allclose(potential, torch.tensor([-40.5568845023]))
  # potential energy test
  # potential = molecule.calculate_potential()
  # assert np.allclose(potential, [-40.5568845023])

  # ionic charge initialization test
  # ion = [['C', [0, 0, 0]], ['O', [0, 3, 0]], ['O', [1, -1, 0]],
  #        ['O', [-1, -1, 0]]]  # Test ionic molecule
  # ionic_molecule = Ferminet(ion, spin=1, charge=-2, seed=0, batch_no=1)
  # _, _, _, _ = ionic_molecule.prepare_input_stream()

  # assert (ionic_molecule.electron_no == np.array([[6], [8], [9], [9]])).all()