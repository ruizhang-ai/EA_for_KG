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
2. For some models, it requires transforming the dataset format. Use the code *transform_data.ipynb* to transform the dataset.
3. To get the result for Experiment 2 and Experiment 3, before running *code_experiment_2.ipynb* and *code_experiment_3.ipynb* you need to export the final embeddings. To do so, you can us the save function from numpy library. For example:
```
#numpy.save(filename, output_embeddings_variable)
numpy.save('output_embeds.npy', outvec)
```
