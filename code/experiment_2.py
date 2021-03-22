import argparse
import pickle
import numpy as np
import scipy
from scipy.spatial import distance

def get_vocab(filename):
	fo = open(filename,"r")
	list_id = list()
	id2ent=dict()
	ent2id=dict()
	counter = 0
	for line in fo:
		line_split = line.split()
		the_id = counter
		the_ent = line_split[1]
		id2ent[int(the_id)] = the_ent
		ent2id[the_ent] = int(the_id)
		list_id.append(int(line_split[0]))
		counter+=1
	fo.close()
	return id2ent, ent2id, list_id

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


	### Load vocab ###
	kb1_vocab_filename = './converted_data/ent_ids_1'
	kb2_vocab_filename = './converted_data/ent_ids_2'
	kb1_id2ent, kb1_ent2id, kb1_ids = get_vocab(kb1_vocab_filename)
	kb2_id2ent, kb2_ent2id, kb2_ids = get_vocab(kb2_vocab_filename)

	### Loas embeddings ###
	all_emb_filename = './output_embeddings/output_embeds.npy'
	all_emb = np.load(all_emb_filename)
	se = all_emb
	se_kb1_emb = np.take(se, kb1_ids, axis=0)
	se_kb2_emb = np.take(all_emb, kb2_ids, axis=0)

	### Compute confidence ###
	fmap = open('./converted_data/ref_ent_ids', 'r')
	confidence_list = list()
	for line in fmap:
		line_split = line.rstrip().split('\t')
		src_ent = int(line_split[0])
		tar_ent = int(line_split[1])-len(se_kb1_emb)
		src_emb = se_kb1_emb[src_ent,:].reshape(1,-1)
		sim = scipy.spatial.distance.cdist(src_emb, se_kb2_emb, metric='cosine') #change metric here
		top_k = sim[0].argsort()[:K]
		if(tar_ent == top_k[0]):
			confidence_list.append(sim[0][top_k[1]] - sim[0][top_k[0]]) # confidence -> second best minus top 
	print (np.mean(confidence_list))
	fmap.close()
