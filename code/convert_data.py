import argparse
import rdflib
from rdflib import Graph, RDFS

def getRelDict(graph):
	rel = dict()
	counter = 0
	for triple in graph:
		s,p,o = triple
		if str(p) not in rel and isinstance(o, rdflib.URIRef):
			rel[str(p)] = counter
			counter += 1
	return rel
	
def get_attr_set(graph):
	attr_set = set()
	for triple in graph:
		s,p,o = triple	
		if isinstance(o, rdflib.Literal):
			attr_set.add(p)
	return attr_set

def get_training_attrs(graph, attr_set):
	training_attrs = set()
	for subject in graph.subjects():
		row = list()
		row.append(str(subject))
		count = 0
		for triple in graph.triples((subject, None, None)):
			s,p,o = triple
			if p in attr_set:
				row.append(str(p))
				count += 1
		if count > 0:
			training_attrs.add('\t'.join(row))
		
	return training_attrs

def get_ent_set(graph):
	ent_set = set()
	for triple in graph:
		s,p,o = triple
		if str(s) not in ent_set:
			ent_set.add(str(s))
		if isinstance(o, rdflib.URIRef) and str(o) not in ent_set:
			ent_set.add(str(o))
	return ent_set

def get_ent_dict(graph, start_id):
	ent_set = get_ent_set(graph)
	count = start_id
	res = dict()
	for e in ent_set:
		res[e] = count
		count += 1
	return res

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


	### Load data ###
	dbp_filename = '../DWY-NB/'+DATASET+'/'+KB1+'_'+KB2+'.ttl'
	kb2_filename = '../DWY-NB/'+DATASET+'/'+KB2+'.ttl'
	map_filename = '../DWY-NB/'+DATASET+'/mapping_'+KB2+'.ttl'
	seed_filename = '../DWY-NB/'+DATASET+'/seed_'+SEED_RATIO+'.ttl'

	dbp_graph = Graph()
	dbp_graph.parse(location=dbp_filename, format='nt')
	kb2_graph = Graph()
	kb2_graph.parse(location=kb2_filename, format='nt')
	map_graph = Graph()
	map_graph.parse(location=map_filename, format='nt')
	seed_graph = Graph()
	seed_graph.parse(location=seed_filename, format='nt')

	#### Get entity dictionary ####
	kb2_ent_ids = get_ent_dict(kb2_graph, 0)
	next_id = max(kb2_ent_ids.values()) + 1
	dbp_ent_ids = get_ent_dict(dbp_graph, next_id)
	
	### Generate "ENT_IDS" ###
	inv_kb2_ent_ids = {v: k for k, v in kb2_ent_ids.items()}
	fw = open('./converted_data/ent_ids_1', 'w')
	for e in sorted(inv_kb2_ent_ids):
		fw.write(str(e)+'\t'+str(inv_kb2_ent_ids[e])+'\n')
	fw.close()
	
	inv_dbp_ent_ids = {v: k for k, v in dbp_ent_ids.items()}
	fw = open('./converted_data/ent_ids_2', 'w')
	for e in sorted(inv_dbp_ent_ids):
		fw.write(str(e)+'\t'+str(inv_dbp_ent_ids[e])+'\n')
	fw.close()
	
	
	### Generate "REF_ENT_IDS" ###
	seeds_file = open('./converted_data/ref_ent_ids', 'w')
	for s_triple in seed_graph:
		s_s, s_p, s_o = s_triple
		seeds_file.write(str(kb2_ent_ids[str(s_o)])+'\t'+str(dbp_ent_ids[str(s_s)])+'\n')

	for triple in map_graph:
		s, p, o = triple
		seeds_file.write(str(kb2_ent_ids[str(o)])+'\t'+str(dbp_ent_ids[str(s)])+'\n')
	seeds_file.close()
	
	### Generate triples ###
	kb2_rel_ids = getRelDict(kb2_graph)
	dbp_rel_ids = getRelDict(dbp_graph)
	
	fw = open('./converted_data/triples_1', 'w')
	for triple in kb2_graph:
		s,p,o = triple	
		if isinstance(o, rdflib.URIRef):
			try:
				fw.write(str(kb2_ent_ids[str(s)]) + '\t' + str(kb2_rel_ids[str(p)]) + '\t' + str(kb2_ent_ids[str(o)])+'\n')
			except:
				continue
	fw.close()
		
	fw = open('./converted_data/triples_2', 'w')
	for triple in dbp_graph:
		s,p,o = triple	
		if isinstance(o, rdflib.URIRef):
			try:
				fw.write(str(dbp_ent_ids[str(s)]) + '\t' + str(dbp_rel_ids[str(p)]) + '\t' + str(dbp_ent_ids[str(o)])+'\n')
			except:
				continue
	fw.close()
		
		
	### Generate attribute data ###
	kb2_attrs = get_attr_set(kb2_graph)
	kb2_training_attrs = get_training_attrs(kb2_graph, kb2_attrs)
	fw1 = open('./converted_data/training_attrs_1', 'w')
	for e in kb2_training_attrs:
		fw1.write(str(e)+'\n')
	fw1.close()
	
	dbp_attrs = get_attr_set(dbp_graph)
	dbp_training_attrs = get_training_attrs(dbp_graph, dbp_attrs)
	fw2 = open('./converted_data/training_attrs_2', 'w')
	for e in dbp_training_attrs:
		fw2.write(str(e)+'\n')
	fw2.close()