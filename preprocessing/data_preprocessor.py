from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline

class InhibitorProcessor:
    class UsefulColumns(BaseEstimator, TransformerMixin):
        def __init__(self, props=None):
            self.props = props
        
        def fit(self, X, y=None):
            # No fitting necessary for this preprocessor
            return self
        
        def transform(self, X):
            # List of molecular properties to include
            columns_to_include = [
                'mw',  # Molecular Weight
                'mf',  # Molecular Formula
                'polararea',  # Polar Surface Area
                'complexity',  # Molecular Complexity
                'xlogp',  # Partition Coefficient
                'heavycnt',  # Heavy Atom Count
                'hbonddonor',  # Hydrogen Bond Donor Count
                'hbondacc',  # Hydrogen Bond Acceptor Count
                'rotbonds',  # Rotatable Bonds Count
                'inchi',  # IUPAC International Chemical Identifier
                'exactmass',  # Exact Mass
                'monoisotopicmass',  # Monoisotopic Mass
                'charge',  # Formal Charge
                'covalentunitcnt',  # Covalent Unit Count
                'isotopeatomcnt',  # Isotope Atom Count
                'totalatomstereocnt',  # Total Atom Stereocenter Count
                'definedatomstereocnt',  # Defined Atom Stereocenter Count
                'undefinedatomstereocnt',  # Undefined Atom Stereocenter Count
                'totalbondstereocnt',  # Total Bond Stereocenter Count
                'definedbondstereocnt',  # Defined Bond Stereocenter Count
                'undefinedbondstereocnt',  # Undefined Bond Stereocenter Count
            ]
            
            if self.props is None:
                self.props = columns_to_include
            
            return X[self.props]

    class DropNaNRows(BaseEstimator, TransformerMixin):
        def fit(self, X, y=None):
            return self
        
        def transform(self, X):
            return X.dropna()

    class RemoveDuplicates(BaseEstimator, TransformerMixin):
        def fit(self, X, y=None):
            return self
        
        def transform(self, X):
            return X.drop_duplicates()

    class AddInhibitorColumn(BaseEstimator, TransformerMixin):
        def fit(self, X, y=None):
            return self
        
        def transform(self, X):
            X['inhibitor'] = 1
            return X

    def __init__(self):
        self.pipeline = Pipeline([
            ('useful_columns', self.UsefulColumns()),
            ('drop_na', self.DropNaNRows()),
            ('remove_duplicates', self.RemoveDuplicates()),
            ('add_inhibitor_descrip', self.AddInhibitorColumn())
        ])

    def process(self, data):
        return self.pipeline.fit_transform(data)

# Example usage
# if __name__ == "__main__":
#     data = pd.DataFrame({
#         'mw': [300, 400, None, 300],
#         'mf': ['C20H30O2', 'C25H35O3', 'C30H40O4', 'C20H30O2'],
#         'polararea': [50, 60, None, 50],
#         'complexity': [200, 250, 300, 200],
#         'xlogp': [3.5, 4.0, 4.5, 3.5],
#         'heavycnt': [20, 25, 30, 20],
#         'hbonddonor': [2, 3, 4, 2],
#         'hbondacc': [4, 5, 6, 4],
#         'rotbonds': [6, 7, 8, 6],
#         'inchi': ['InChI=1S/C20H30O2', 'InChI=1S/C25H35O3', 'InChI=1S/C30H40O4', 'InChI=1S/C20H30O2'],
#         'isosmiles': ['CC(C)CC1=CC=CC=C1', 'CC(C)CC2=CC=CC=C2', 'CC(C)CC3=CC=CC=C3', 'CC(C)CC1=CC=CC=C1'],
#         'canonicalsmiles': ['CC(C)CC1=CC=CC=C1', 'CC(C)CC2=CC=CC=C2', 'CC(C)CC3=CC=CC=C3', 'CC(C)CC1=CC=CC=C1'],
#         'exactmass': [300.224, 400.324, 500.424, 300.224],
#         'monoisotopicmass': [300.224, 400.324, 500.424, 300.224],
#         'charge': [0, 0, 0, 0],
#         'covalentunitcnt': [1, 1, 1, 1],
#         'isotopeatomcnt': [0, 0, 0, 0],
#         'totalatomstereocnt': [0, 0, 0, 0],
#         'definedatomstereocnt': [0, 0, 0, 0],
#         'undefinedatomstereocnt': [0, 0, 0, 0],
#         'totalbondstereocnt': [0, 0, 0, 0],
#         'definedbondstereocnt': [0, 0, 0, 0],
#         'undefinedbondstereocnt': [0, 0, 0, 0],
#         'pclidcnt': [1, 1, 1, 1],
#         'gpidcnt': [1, 1, 1, 1],
#         'gpfamilycnt': [1, 1, 1, 1],
#         'neighbortype': ['type1', 'type2', 'type3', 'type1']
#     })

#     processor = InhibitorProcessor()
#     processed_data = processor.process(data)
#     print(processed_data)