## DWY-NB Benchmark
**DWY-NB** is a new benchmark for entity alignment between knowledge graphs. This benchmark consists of two datasets; each dataset consists of a pair of KGs that can be used for the evaluation of EA techniques. We call the two datasets DY-NB and DW-NB. The two KGs of `DY-NB` are subsets of *DBpedia [Auer et al., 2007]* and *Yago [Hoffart et al., 2013]*, respectively. The two KGs of `DW-NB` are subsets of DBpedia and *Wikidata [Vrandecic and Krotzsch, 2014]*, respectively.

### Predicate alignment

## What are in this Repository
This repository contains the following contents:
```
/
├── DWY-NB/                 --> (The benchmark datasets folder)
|   ├── DW-NB/              --> (The DW-NB dataset. It contains a KG-pair of DBpedia and Wikidata)
|   |   ├── dbp_wd.ttl      --> (The subset of DBpedia KG)
|   |   ├── mapping_wd      --> (The known entity alignment as testing data)
|   |   ├── seed_10.ttl     --> (The seed entity alignment with the ratio of 10%)
|   |   ├── seed_20.ttl     --> (The seed entity alignment with the ratio of 20%)
|   |   ├── seed_30.ttl     --> (The seed entity alignment with the ratio of 30%)
|   |   ├── seed_40.ttl     --> (The seed entity alignment with the ratio of 40%)
|   |   ├── seed_50.ttl     --> (The seed entity alignment with the ratio of 50%)
|   |   └── wd.ttl          --> (The subset of Wikidata KG)
|   └── DY-NB/              --> (The DY-NB dataset. It contains a KG-pair of DBpedia and YAGO)
|   |   ├── dbp_yago.ttl    --> (The subset of DBpedia KG)
|   |   ├── mapping_yago    --> (The known entity alignment as testing data)
|   |   ├── seed_10.ttl     --> (The seed entity alignment with the ratio of 10%)
|   |   ├── seed_20.ttl     --> (The seed entity alignment with the ratio of 20%)
|   |   ├── seed_30.ttl     --> (The seed entity alignment with the ratio of 30%)
|   |   ├── seed_40.ttl     --> (The seed entity alignment with the ratio of 40%)
|   |   ├── seed_50.ttl     --> (The seed entity alignment with the ratio of 50%)
|   |   └── yago.ttl        --> (The subset of YAGO KG)
├── code/                   --> (A folder containing source codes used for the experiments)   
├── LICENCE                 --> (The licence file)
└── README.md               --> (The readme file)
```

## Citation
If you use the datasets in the DWY-NB Benchmark, please credit us by citing the following papers:

* *Bayu Distiawan Trisedya, Jianzhong Qi, and Rui Zhang. "Entity alignment between knowledge graphs using attribute embeddings." In Proceedings of the AAAI Conference on Artificial Intelligence, vol. 33, no. 01, pp. 297-304. 2019.*
* *Rui Zhang, Bayu Distiawan Trisedya, Miao Li, Yong Jiang and Jianzhong Qi. "A  Comprehensive  Survey  on  Knowledge  Graph  EntityAlignment via Representation Learning". In arXiv. 2021.*

```
@inproceedings{trisedya2019entity,
  title={Entity alignment between knowledge graphs using attribute embeddings},
  author={Bayu Distiawan Trisedya and Qi, Jianzhong and Zhang, Rui},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  volume={33},
  number={01},
  pages={297--304},
  year={2019}
}

@inproceedings{zhang2021survey,
  title={A  Comprehensive  Survey  on  Knowledge  Graph  EntityAlignment via Representation Learning},
  author={Rui Zhang and Bayu Distiawan Trisedya and Miao Li and Yong Jiang and Jianzhong Qi},
  booktitle={arXiv},
  year={2021}
}
```
