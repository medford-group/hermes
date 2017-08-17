import unittest


import sys
sys.path.insert(0,'..')
from hermes.convert import atoms_to_dict, dict_to_atoms, data_to_dict, dict_to_data

from ase import Atoms
from ase.build import surface
from ase.constraints import Hookean, FixAtoms, FixBondLength

class ConversionConsistency(unittest.TestCase):
    """Tests for consistency between data conversions"""

    def get_test_atoms(self):
	a = 4.0
	Pt3Rh = Atoms('Pt3Rh',
		      scaled_positions=[(0, 0, 0),
					(0.5, 0.5, 0),
					(0.5, 0, 0.5),
					(0, 0.5, 0.5)],
		      cell=[a, a, a],
		      pbc=True)
	s3 = surface(Pt3Rh, (2, 1, 1), 9)
	s3.center(vacuum=10, axis=2)

	s3.rattle()

	hook = Hookean(a1=0, a2=1, rt=4, k=5)
	fix = FixAtoms(mask=[a.symbol == 'Rh' for a in s3])
	fbl = FixBondLength(1,2)

	s3.set_constraint([fix, fbl, hook])

	return s3

    def test_atoms_dict(self):
	atoms = self.get_test_atoms()
	d = atoms_to_dict(atoms)
        a = dict_to_atoms(d)

        self.assertEqual(atoms, a)


if __name__ == '__main__':
    unittest.main()
