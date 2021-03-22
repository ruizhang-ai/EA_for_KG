## Directory structure
This directory contains the following contents:
```
code/
├── converted_data/           --> (A folder for storing the converted data used as input for an EA technique)
├── output_embeddings/        --> (A folder for storing the resulting embeddings of an EA technique)   
├── resource/                 
│   └── dbp_ent2type.pickle   --> (A resource file containing the type of entities in the DBpedia knowledge graph)
├── experiment_2.py           --> (The code for running experiment 2 in the survey paper)
├── experiment_3.py           --> (The code for running experiment 3 in the survey paper)
└── transform_data.py         --> (The code for transforming KGs into the data structured as required by an EA technique)
```

## Below is the list the EA techniques compared in the experiments

* MTransE: https://github.com/muhaochen/MTransE
* ITransE: https://github.com/thunlp/IEAJKE
* BootEA: https://github.com/nju-websoft/BootEA
* TransEdge: https://github.com/nju-websoft/TransEdge
* JAPE: https://github.com/nju-websoft/JAPE
* MultiKE: https://github.com/nju-websoft/MultiKE
* AttrE: https://bitbucket.org/bayudt/kba/src
* MuGNN: https://github.com/thunlp/MuGNN
* AliNET: https://github.com/nju-websoft/AliNet
* KECG: https://github.com/THU-KEG/KECG
* GCN-Align: https://github.com/1049451037/GCN-Align
* HGCN: https://github.com/StephanieWyt/HGCN-JE-JR
* GMNN: https://github.com/syxu828/Crosslingula-KG-Matching
* RDGCN: https://github.com/StephanieWyt/RDGCN
* CEA: https://github.com/DexterZeng/CEA
* MRAEA: https://github.com/MaoXinn/MRAEA
* NMN: https://github.com/StephanieWyt/NMN


## Instruction to reproduce the experimental results in the survey paper
1. Download the EA technique codes from the list above.
2. The datasets in DYW-NB benchmark contain a pair of KGs. For each KG, the data are store in the form of triple `<subject, predicate, object>`. Some EA techniques require the input to be in a different format. To run their code, we need to convert the data from the DWY-NB into the required format. Use the following command to convert the dataset.
   <pre><code>python transform_data.py --seed [Seed Ratio] --dataset [Dataset Folder]
   for example:
   <b>python transform_data.py --seed 30 --dataset DY-NB</b></code></pre>
3. To run the Experiment 1 in the survey paper, please follow the command for each technique.
     <pre><code>[Below is the sample of running GCN-Align over our dataset]
     python train_kba.py --lang converted_data --seed 4500
4. Before running *experiment_2.py* and *experiment_3.py*, you need to export the final embeddings for each technique. To do so, you can use the *save* function from numpy library as follows:
   <pre><code>[The sample below is from the file <b>train.py</b> in GCN-Align]
   ...
   # Testing
   feed_dict_ae = construct_feed_dict(ae_input, support, ph_ae)
   feed_dict_se = construct_feed_dict(1.0, support, ph_se)
   vec_ae = sess.run(model_ae.outputs, feed_dict=feed_dict_ae)
   vec_se = sess.run(model_se.outputs, feed_dict=feed_dict_se)
   <b>np.save('./output_embeddings/output_embeds.npy', vec_se)</b>  <-- add this line to export the embeddings
   ...</code></pre>
5. To run the *experiment_2.py* and *experiment_3.py*, please use the following command:
   * Experiment 2
     <pre><code>python experiment_2.py --seed [Seed Ratio] --dataset [Dataset Folder]
     for example:
     <b>python experiment_2.py --seed 30 --dataset DY-NB</b></code></pre>
   * Experiment 3
     <pre><code>python experiment_3.py --seed [Seed Ratio] --dataset [Dataset Folder]
     for example:
     <b>python experiment_3.py --seed 30 --dataset DY-NB</b></code></pre>
6. To run the Experiment 4 in the survey paper, please follow the command for each technique.
     <pre><code>[Below is the sample of running GCN-Align over our dataset]
     python train_kba.py --lang converted_data --seed 4500
