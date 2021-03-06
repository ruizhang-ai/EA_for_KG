## Directory structure
This directory contains the following contents:
```
code/
├── converted_data/           --> (A folder for storing the converted data used as input for an EA technique)
├── output_embeddings/        --> (A folder for storing the resulting embeddings of an EA technique)   
├── resource/                 
│   └── dbp_ent2type.pickle   --> (A resource file containing the type of entities in the DBpedia knowledge graph)
├── convert_data.py           --> (The code for converting KGs into the data structured as required by an EA technique)
├── experiment_2.py           --> (The code for running experiment 2 in the survey paper)
└── experiment_3.py           --> (The code for running experiment 3 in the survey paper)
```

## Below is the list the EA techniques compared in the experimental study of the paper [[Zhang et al. 2021]](https://arxiv.org/abs/2103.15059)

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


## Instructions for reproducing the experiments in the paper [[Zhang et al. 2021]](https://arxiv.org/abs/2103.15059)
0. You need to set up the environment for running the experiments (Anaconda 3-2020.02 or above and Python 3.7 or above). First, you can install Anaconda by following the instruction from  the website below:
   <pre><code>https://docs.anaconda.com/anaconda/install/</code></pre>
   Next, you can create a virtual environment using the following commands:
   <pre><code>conda create -n kga python=3.7 anaconda
   conda activate kga</code></pre>

1. Download the EA technique code from the list above and the benchmark DYW-NB. For example:
   <pre><code>GCN-Align: git clone https://github.com/1049451037/GCN-Align.git
   DYW-NB: git clone https://github.com/ruizhang-ai/EA_for_KG.git</code></pre>
2. The datasets in DYW-NB benchmark contain a pair of KGs. For each KG, the data are stored in the form of triples `<subject, predicate, object>`. Some EA techniques require the input to be in different formats. To run their code, we need to convert the data from DWY-NB into the data formats required by those techniques. Use the following command to convert the dataset for those techniques.
   <pre><code>python convert_data.py --seed [Seed Ratio] --dataset [Dataset Folder]
   for example:
   <b>python convert_data.py --seed 30 --dataset DY-NB</b></code></pre>
   
   After converting the data, you can copy them to the folder "data" in the directory of the EA technique downloaded in step 1. Note that different EA techniques may use different names of the "data". Please refer to each EA technique's instruction.
   <pre><code>cp -r converted_data/ GCN-Align/data/</code></pre>
   
3. To run `Experiment 1` in the paper, use the command for each technique provided by their respective instructions following the URLs given above.
   <pre><code>[Below is an example of running GCN-Align on our dataset]
   <b>python train_kba.py --lang converted_data --seed 4500</b></code></pre>
4. Before running `Experiment 2` and `Experiment 3`, you need to export the final embeddings for each EA technique. To do so, you can use the *save* function from numpy library as follows:
   <pre><code>[The sample below is from the file <b>train.py</b> in GCN-Align]
   ...
   # Testing
   feed_dict_ae = construct_feed_dict(ae_input, support, ph_ae)
   feed_dict_se = construct_feed_dict(1.0, support, ph_se)
   vec_ae = sess.run(model_ae.outputs, feed_dict=feed_dict_ae)
   vec_se = sess.run(model_se.outputs, feed_dict=feed_dict_se)
   <b>np.save('../output_embeddings/output_embeds.npy', vec_se)</b>  <-- add this line to export the embeddings
   ...</code></pre>
5. To run `Experiment 2` and `Experiment 3`, use the following command:
   * Experiment 2
     <pre><code>python experiment_2.py --seed [Seed Ratio] --dataset [Dataset Folder]
     for example:
     <b>python experiment_2.py --seed 30 --dataset DY-NB</b></code></pre>
   * Experiment 3
     <pre><code>python experiment_3.py --seed [Seed Ratio] --dataset [Dataset Folder]
     for example:
     <b>python experiment_3.py --seed 30 --dataset DY-NB</b></code></pre>
6. To run `Experiment 4` in the paper, use the command for each technique provided by their respective instructions following the URLs given above.
   <pre><code>[Below is the sample of running GCN-Align over our dataset]
   <b>python train_kba.py --lang converted_data --seed 4500</b></code></pre>
