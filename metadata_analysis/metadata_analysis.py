import glob
import json
import logging
import os
import re
import subprocess

import pandas as pd
import scispacy
import spacy
import yake

logging.basicConfig(level=logging.INFO)
metadata_dictionary = {}


def querying_pygetpapers_sectioning(query, hits, output_directory, using_terms=False, terms_txt=None):
    """queries pygetpapers for specified query. Downloads XML, and sections papers using ami section

    Args:
        query (str): query to pygetpapers
        hits (int): no. of papers to download
        output_directory (str): CProject Directory (where papers get downloaded)
        using_terms (bool, optional): pygetpapers --terms flag. Defaults to False.
        terms_txt (str, optional): path to text file with terms. Defaults to None.
    """
    logging.info('querying pygetpapers')
    if using_terms:
        subprocess.run(f'pygetpapers -q "{query}" -k {hits} -o {output_directory} -x --terms {terms_txt} --logfile pygetpapers_log.txt',
                       shell=True)
    else:
        subprocess.run(f'pygetpapers -q "{query}" -k {hits} -o {output_directory} -x  --logfile pygetpapers_log.txt',
                       shell=True)
    logging.info('running ami section')
    subprocess.run(f'ami -p {output_directory} section', shell=True)


def get_metadata_json(output_directory):
    WORKING_DIRECTORY = os.getcwd()
    glob_results = glob.glob(os.path.join(WORKING_DIRECTORY,
                                          output_directory, "*", 'eupmc_result.json'))
    metadata_dictionary["metadata_json"] = glob_results


def get_PMCIDS(metadata_dictionary=metadata_dictionary):
    PMCIDS = []
    for result in metadata_dictionary["metadata_json"]:
        split_path = result.split('\\')
        r = re.compile(".*PMC")
        PMCID = (list(filter(r.match, split_path)))
        PMCIDS.extend(PMCID)
    metadata_dictionary["PMCIDS"] = PMCIDS
    logging.info('getting PMCIDs')


def get_abstract(metadata_dictionary=metadata_dictionary):
    TAG_RE = re.compile(r"<[^>]+>")
    abstract_list = []
    for metadata in metadata_dictionary["metadata_json"]:
        with open(metadata) as f:
            metadata_in_json = json.load(f)
            try:
                raw_abstract = metadata_in_json["full"]["abstractText"]
                abstract = TAG_RE.sub(' ', raw_abstract)
                abstract_list.append(abstract)
            except KeyError:
                abstract_list.append('NaN')
    metadata_dictionary["abstract"] = abstract_list
    logging.info("getting the abstracts")


def get_keywords(metadata_dictionary=metadata_dictionary):
    keywords_list = []
    for metadata in metadata_dictionary["metadata_json"]:
        with open(metadata) as f:
            metadata_in_json = json.load(f)
            try:
                keywords_list.append(
                    metadata_in_json["full"]["keywordList"]["keyword"])
            except KeyError:
                keywords_list.append('NaN')
    metadata_dictionary["keywords"] = keywords_list
    logging.info("getting the keywords")


def key_phrase_extraction(metadata_dictionary=metadata_dictionary):
    keywords_all = []
    for abstract in metadata_dictionary["abstract"]:
        custom_kw_extractor = yake.KeywordExtractor(
            lan='en', n=2, top=10, features=None)
        keywords = custom_kw_extractor.extract_keywords(abstract)
        keywords_list = []
        for kw in keywords:
            keywords_list.append(kw[0])
        keywords_all.append(keywords_list)
    metadata_dictionary["yake_keywords"] = keywords_all
    logging.info('extracted key phrases')
    return metadata_dictionary


def get_organism(metadata_dictionary=metadata_dictionary):
    nlp = spacy.load("en_ner_bionlp13cg_md")
    all_entities = []
    for abstract in metadata_dictionary["abstract"]:
        entity = []
        doc = nlp(abstract)
        for ent in doc.ents:
            if ent.label_ == 'GENE_OR_GENE_PRODUCT':
                entity.append(ent)
        all_entities.append(entity)
    metadata_dictionary["entities"] = all_entities
    logging.info("NER using SciSpacy - looking for ORGANISMS")


def convert_to_csv(path='keywords_abstract_yake_organism_pmcid_tps_cam_ter.csv', metadata_dictionary=metadata_dictionary):
    df = pd.DataFrame(metadata_dictionary)
    df.to_csv(path, encoding='utf-8', line_terminator='\r\n')
    logging.info(f'writing the keywords to {path}')


def look_for_tps(metadata_dictionary=metadata_dictionary, search_for="TPS"):
    all_matches = []
    for abstract in metadata_dictionary["abstract"]:
        words = abstract.split(" ")
        match_list = ([s for s in words if f"{search_for}" in s])
        all_matches.append(match_list)
    metadata_dictionary[f"{search_for}_match"] = all_matches
    logging.info(f"looking for {search_for} in abstract")


def add_if_file_contains_terms(metadata_dictionary=metadata_dictionary, terms=['terpene synthase']):
    metadata_dictionary["terms"] = []
    for term in terms:
        for abstract in metadata_dictionary["abstract"]:
            if term.lower() in abstract.lower():
                metadata_dictionary["terms"].append(term)
            else:
                metadata_dictionary["terms"].append('NaN')
    logging.info('looking for term matches')


# Calling all functions
CPROJECT = os.path.join(os.getcwd(), 'corpus', 'tps_camellia')
# querying_pygetpapers_sectioning("terpene synthase volatile Camellia AND (((SRC:MED OR SRC:PMC OR SRC:AGR OR SRC:CBA) NOT (PUB_TYPE:'Review')))",
# '100',
#  CPROJECT)
get_metadata_json(CPROJECT)
get_PMCIDS()
get_abstract()
get_keywords()
key_phrase_extraction()
get_organism()
look_for_tps()
look_for_tps(search_for='Camellia')
add_if_file_contains_terms()
convert_to_csv()
