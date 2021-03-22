import argparse
import pickle
import numpy as np
from sklearn import preprocessing
from sklearn import svm
from sklearn.model_selection import cross_val_score


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-seed", "--seed", dest = "seed", default = "30", help="Seed ratio")
	parser.add_argument("-dataset", "--dataset", dest = "dataset", default = "DW-NB", help="Dataset name")
	args = parser.parse_args()
	
	### Defined variables ### 
	KB1 = "dbp"
	if args.dataset == "DW-NB":
		KB2 = "wd"
	else:
		KB2 = "yago"
	SEED_RATIO = args.seed
	DATASET = args.dataset
	K = 10


	### Load  data ###
	ent2type = pickle.load(open("./resource/dbp_ent2type.pickle", "rb")) # load entity type
	emb = np.load('./output_embeddings/output_embeds.npy') # load embeddings
	# load entity id
	dbp_id_ent = dict()
	with open('./converted_data/ent_ids_2', 'r') as f:
		for line in f.readlines():
			line = line.rstrip().split('\t')
			idx = int(line[0])
			ent = line[1]
			dbp_id_ent[idx] = ent
	#load entity type id
	dbp_id_ent_type = dict()
	for idx, ent in dbp_id_ent.items():
		try:
			ent_type = ent2type[ent]
			dbp_id_ent_type[idx] = ent_type
		except:
			continue
	type_dict = dict()
	counter = 0
	for ent_type in dbp_id_ent_type.values():
		if ent_type not in type_dict:
			type_dict[ent_type] = counter
			counter += 1

	### Create training and testing data ###
	my_data = list()
	my_type = list()
	for idx, ent_type_txt in dbp_id_ent_type.items():
		my_data.append(emb[idx])
		my_type.append(type_dict[ent_type_txt])
	X = np.asarray(my_data)
	y = np.asarray(my_type)

	
	### TEST ###
	print ("Start Testing")
	clf = svm.SVC(verbose=3)
	scores = cross_val_score(clf, X, y, cv=2)
	print("Accuracy: %0.4f (+/- %0.4f)" % (scores.mean(), scores.std() * 2))