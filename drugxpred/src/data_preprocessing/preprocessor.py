class KnownInhibitorsPreprocessor:
    def __init__(self):
        # Initialize the preprocessor
        pass
    
    def filter_mol_props(self, data, props=None):
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
            'isosmiles',  # Isomeric SMILES
            'canonicalsmiles',  # Canonical SMILES
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
            'pclidcnt',  # PubChem Compound ID Count
            'gpidcnt',  # Gene Product ID Count
            'gpfamilycnt',  # Gene Product Family Count
            'neighbortype'  # Neighbor Type
        ]
        
        if props is None:
            props = columns_to_include
        
        return data[props]