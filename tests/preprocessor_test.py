import pytest
import pandas as pd
from preprocessing.data_preprocessor import InhibitorProcessor

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'mw': [300, 400, None, 300],
        'mf': ['C20H30O2', 'C25H35O3', 'C30H40O4', 'C20H30O2'],
        'polararea': [50, 60, None, 50],
        'complexity': [200, 250, 300, 200],
        'xlogp': [3.5, 4.0, 4.5, 3.5],
        'heavycnt': [20, 25, 30, 20],
        'hbonddonor': [2, 3, 4, 2],
        'hbondacc': [4, 5, 6, 4],
        'rotbonds': [6, 7, 8, 6],
        'inchi': ['InChI=1S/C20H30O2', 'InChI=1S/C25H35O3', 'InChI=1S/C30H40O4', 'InChI=1S/C20H30O2'],
        'isosmiles': ['CC(C)CC1=CC=CC=C1', 'CC(C)CC2=CC=CC=C2', 'CC(C)CC3=CC=CC=C3', 'CC(C)CC1=CC=CC=C1'],
        'canonicalsmiles': ['CC(C)CC1=CC=CC=C1', 'CC(C)CC2=CC=CC=C2', 'CC(C)CC3=CC=CC=C3', 'CC(C)CC1=CC=CC=C1'],
        'exactmass': [300.224, 400.324, 500.424, 300.224],
        'monoisotopicmass': [300.224, 400.324, 500.424, 300.224],
        'charge': [0, 0, 0, 0],
        'covalentunitcnt': [1, 1, 1, 1],
        'isotopeatomcnt': [0, 0, 0, 0],
        'totalatomstereocnt': [0, 0, 0, 0],
        'definedatomstereocnt': [0, 0, 0, 0],
        'undefinedatomstereocnt': [0, 0, 0, 0],
        'totalbondstereocnt': [0, 0, 0, 0],
        'definedbondstereocnt': [0, 0, 0, 0],
        'undefinedbondstereocnt': [0, 0, 0, 0],
        'pclidcnt': [1, 1, 1, 1],
        'gpidcnt': [1, 1, 1, 1],
        'gpfamilycnt': [1, 1, 1, 1],
        'neighbortype': ['type1', 'type2', 'type3', 'type1']
    })

def test_preprocessor(sample_data):
    preprocessor = InhibitorProcessor()
    processed_data = preprocessor.process(sample_data)
    
    # Check if the 'inhibitor' column is added
    assert 'inhibitor' in processed_data.columns
    
    # Check if all values in the 'inhibitor' column are 1
    assert all(processed_data['inhibitor'] == 1)
    
    # Check if NaN values are dropped
    assert processed_data.isna().sum().sum() == 0
    
    # Check if duplicates are removed
    assert processed_data.duplicated().sum() == 0