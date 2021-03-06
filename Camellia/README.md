# This folder contains following files:

A) **CamelliaTPS folder**: Corpus that is created by using command **pygetpapers -q "terpene synthase volatile Camellia AND (((SRC:MED OR SRC:PMC OR SRC:AGR OR SRC:CBA) NOT (PUB_TYPE:"Review")))" -o CamelliaTPS -x -p -s**

B) **CamelliaTPS_from_corpus**: csv file containing terms extracted from corpus.

C) **Camellia_TPS**: csv file with TPS gene's information such as uniprot ID, uniprotkb ac/ID, Organism name, synonyms and corresponding TPS protein function etc. This file is created using Uniprot database.

D) **eo_CAMPSITps.xml**: **Dictionary Summary** 

| Dictionary specifications |Number |% |
   | --- | --- | --- |
   |Total Terms | 285| |
   |Terms with synonyms |14| 5% |
   |Terms with Wikidata IDs| 71| 25% |
   |Cammelia specific terms|81 | 28% |

E) **full data table**: full data table generated after testing dictionary. Please, refer https://github.com/petermr/crops/wiki/TPS-Reserve-For-Camellia-and-Tomato-Crop
