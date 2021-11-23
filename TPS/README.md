## This folder contains following files that are created while working on TPS enzyme collection:

A) **11951_TPS** csv file contains total 11951 TPS genes that are collected from Uniprot and phytozome. Please refer https://github.com/petermr/CEVOpen/wiki/GENE-:-TPS 

B) **TPS_EC** (for TPS enzyme commission number) csv file contain TPS enzyme names and EC number.

C) **TPS metadata analysis.csv** -
 
I ran metadata_analysis.py script (https://github.com/petermr/crops/blob/main/metadata_analysis/metadata_analysis.py) on **corpus PlantTPS** (present in this folder, contains 573 papers). In this metadata_analysis.py script, it uses command **pygetpapers -q "terpene synthase TPS plant" -o TPS -p**

Metadata analysis script 

- **queries EPMC via pygetpapers, downloads XML and creates Corpus**.
- sections papers using ami-section
- gets the PMCIDs, Abstracts and Keywords from the metadata of individual papers
- globs and parses the XML to get the section of your interest (result, method, etc.)
- extracts key phrases from that section using YAKE
- recognizes entities (like organism, chemical, gene, gene product, and so on) using scispacy
- splits the section paragraphs of indivdiual papers into a list of words and looks for a particular string ('TPS' or 'citrus' for example) in the words and retreives them
- matches against a given set of phrases (like terpene synthase, terponoids, or species name) and retrieves them for each para
- **outputs all the analysis as a .csv** (find TPS metadata analysis.csv) for interprations and conclusions. A typical output is available here. Since it's too large of a file for GitHub to display on GUI, you would   have to download it to view.

D) **wiki_binomial_abbreviation** (for abbreviation of scientific name) csv file contain Scientific names of essential oil plants, their wikidata IDs and abbreviations.
