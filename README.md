## DWY-NB Benchmark
**DWY-NB** is a benchmark for entity alignment (EA) between knowledge graphs (KGs). This benchmark consists of two datasets `DY-NB` and `DW-NB`; each dataset consists of a pair of KGs that can be used for the evaluation of EA techniques. The two KGs of `DY-NB` are subsets of *DBpedia [Auer et al., 2007]* and *Yago [Hoffart et al., 2013]*, respectively. The two KGs of `DW-NB` are subsets of DBpedia and *Wikidata [Vrandecic and Krotzsch, 2014]*, respectively. More about this benchmark such as the background and how it is generated are described in [*[Rui Zhang, Bayu Distiawan Trisedya, Miao Li, Yong Jiang and Jianzhong Qi. "A  Benchmark and Comprehensive  Survey  on  Knowledge  Graph  Entity Alignment via Representation Learning". to appear in VLDB Journal, 2022.]*](https://arxiv.org/abs/2103.15059).

### Notes on predicate alignment in the benchmark
  Note that many techniques use manually created seed attribute/relation predicate alignments which positively impact the performance, while some other techniques do not. To be able to isolate the effect of the factor being evaluated for a certain experiment in our experimental study (e.g., the effect of seed entity alignments proportions, the effect of attribute triples, etc.) reported in [Zhang et al. 2021], we have aligned the predicates between the KGs in those experiments so that predicate alignments have the same effect on the performance of all the techniques no matter whether they take some measures to align predicates. If we did not align the predicates in our data, then the techniques that do not take measures to align predicates might have poorer performance due to unaligned predicates rather than due to the effect of the factor being evaluated. Below is the procedure we use to aligned the predicate in the datasets.

1. List all candidate predicate alignments by extracting all pairs of predicates from two KGs.
2. To compute the predicate similarity, we use `SequenceMatcher` from `difflib` in `Python`. Below is the sample instruction to compute predicate similarity using `SequenceMatcher`: 
   * Install python-Levenshtein
      ```
      pip install python-Levenshtein
      ```
   * Compute the similarity of all possible predicate pairs between two KGs. To compute the similarity, you can use the following command:
      ```
      import difflib
      ...
      pred_similarity=difflib.SequenceMatcher("predicate_1", "predicate_2").ratio()
      ...
3. Filter the predicate similarity (*pred_similarity*) using a certain threshold to get the candidate predicate alignments. We use the threshold of 0.80 to get a high recall.
4. Manually remove the false-positives from the candidate predicate alignments.


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
├── code/                   --> (A folder containing source code used for the experiments)   
├── LICENCE                 --> (The licence file)
└── README.md               --> (The readme file)
```

## Citation
If you use the datasets in the DWY-NB Benchmark, please credit us by citing the following papers:

* [Trisedya et al. 2019] *Bayu Distiawan Trisedya, Jianzhong Qi, and Rui Zhang. "Entity alignment between knowledge graphs using attribute embeddings." In Proceedings of the AAAI Conference on Artificial Intelligence, vol. 33, no. 01, pp. 297-304 (2019).*
* [Zhang et al. 2021] *Rui Zhang, Bayu Distiawan Trisedya, Miao Li, Yong Jiang and Jianzhong Qi. "A  Benchmark and Comprehensive  Survey  on  Knowledge  Graph  Entity Alignment via Representation Learning". VLDB Journal, 2022.*

```
@inproceedings{trisedya2019entity,
  title={Entity alignment between knowledge graphs using attribute embeddings},
  author={Bayu Distiawan Trisedya and Qi, Jianzhong and Zhang, Rui},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  pages={297--304},
  year={2019}
}

@inproceedings{zhang2021survey,
  title={A  Benchmark and Comprehensive  Survey  on  Knowledge  Graph  EntityAlignment via Representation Learning},
  author={Rui Zhang and Bayu Distiawan Trisedya and Miao Li and Yong Jiang and Jianzhong Qi},
  archivePrefix={arXiv preprint},
  eprint={arXiv:2103.15059}
  year={2021}
}
```
