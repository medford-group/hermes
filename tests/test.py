import unittest

import sys
sys.path.insert(0,'..')
from hermes.convert import atoms_to_dict, dict_to_atoms, calc_to_dict, dict_to_calc, data_to_dict, dict_to_data
from hermes.mongo import Mongo_query, Mongo_insert_one,Mongo_delete

from ase import Atoms
from ase.build import surface
from ase.constraints import Hookean, FixAtoms, FixBondLength
from espresso import espresso

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

    def get_test_calcs(self):
        esp_settings = dict(atoms=None, 
                            pw=350.0,
                            dw=3500,
                            nbands=-10,
                            kpts=(1,1,1), 
                            kptshift=(0,0,0),
                            mode='ase3',
                            opt_algorithm='ase3',
                            fmax=0.05,
                            xc='PBE',
                            smearing='fd',
                            sigma=0.1,
                            U_projection_type='atomic',
                            occupations='smearing',
                            dipole={'status': False},
                            field={'status': False},
                            convergence={'energy': 1e-6,'mixing': 0.7,'maxsteps': 100,'diag': 'david'}, 
                            verbose='low')
        esp = espresso(**esp_settings)

        return [esp] #return list in case we add more calcs in the future

    def test_atoms_dict(self):
        atoms = self.get_test_atoms()
        d = atoms_to_dict(atoms)
        a = dict_to_atoms(d)

        self.assertEqual(atoms, a)

    def test_calc_dict(self):
        calcs = self.get_test_calcs()
        for ci in calcs:
            print('Testing: {}'.format(ci))
            d = calc_to_dict(ci)
            c = dict_to_calc(d)
            self.assertEqual(ci.todict(), c.todict())
            self.assertNotEqual(ci.todict(),{})
            
            
            
class MongoConnectivity(unittest.TestCase):
    def get_test_case(self):
        return {'test':'test'}
    def test_mongo_connection(self):
        test_dict = self.get_test_case()
        Mongo_insert_one(test_dict,database = 'medford-data', collection = 'test', username = None, password = None)
        Mongo_query(database = 'medford-data', collection = 'test', query = {}, username = None, password = None,printout = False)
        Mongo_delete({'test':'test'},database = 'medford-data', collection = 'test', username = None, password = None)
        


if __name__ == '__main__':
    unittest.main()
