import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.DataStructs.cDataStructs import TanimotoSimilarity
from sklearn.neighbors import KNeighborsClassifier

class TanimotoKNN:
    def __init__(self, n_neighbors=5, threshold=0.85):
        self.n_neighbors = n_neighbors
        self.threshold = threshold
        self.knn = KNeighborsClassifier(n_neighbors=n_neighbors, metric='precomputed')
    
    def compute_fingerprints(self, smiles_list):
        fingerprints = []
        for smi in smiles_list:
            mol = Chem.MolFromSmiles(smi)
            fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=2048)
            fingerprints.append(fp)
        return fingerprints

    def tanimoto_similarity_matrix(self, fps):
        num_molecules = len(fps)
        sim_matrix = []
        for i in range(num_molecules):
            sims = [TanimotoSimilarity(fps[i], fps[j]) for j in range(num_molecules)]
            sim_matrix.append(sims)
        return sim_matrix

    def fit(self, known_inhibitors_file):
        known_inhibitors = pd.read_csv(known_inhibitors_file)
        inhibitor_smiles = known_inhibitors['SMILES']
        inhibitor_fingerprints = self.compute_fingerprints(inhibitor_smiles)
        inhibitor_sim_matrix = self.tanimoto_similarity_matrix(inhibitor_fingerprints)
        self.knn.fit(inhibitor_sim_matrix, [1] * len(inhibitor_fingerprints))
        self.inhibitor_fingerprints = inhibitor_fingerprints

    def predict(self, screening_library_file, output_file):
        screening_library = pd.read_csv(screening_library_file)
        library_smiles = screening_library['SMILES']
        library_fingerprints = self.compute_fingerprints(library_smiles)
        
        test_sim_matrix = []
        for lib_fp in library_fingerprints:
            sims = [TanimotoSimilarity(lib_fp, inhibitor_fp) for inhibitor_fp in self.inhibitor_fingerprints]
            test_sim_matrix.append(sims)
        
        distances, indices = self.knn.kneighbors(test_sim_matrix)
        
        predictions = []
        for dist in distances:
            max_similarity = max(dist)
            if max_similarity < self.threshold:
                predictions.append(0)
            else:
                predictions.append(1)
        
        screening_library['Prediction'] = predictions
        screening_library.to_csv(output_file, index=False)

# Example usage:
# tanimoto_knn = TanimotoKNN()
# tanimoto_knn.fit('known_inhibitors.csv')
# tanimoto_knn.predict('screening_library.csv', 'classified_compounds.csv')
