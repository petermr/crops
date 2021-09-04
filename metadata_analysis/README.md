## Inspiration

I got the idea to write [`metadata_analysis.py`](https://github.com/petermr/crops/blob/main/metadata_analysis/metadata_analysis.py)(wrongly named since it analysis full text as well. Better name suggestion?) script on Thursday(20210902) when we were discussing KARYA Interns task. So, the task here was to manually scavenge through a corpus of papers for TPS genes of a plant/crop. Manually looking for TPS gene to me sounded like a mundane task that had a potential to be automated. 
## What does the script do?
So, this script:
- queries EPMC via `pygetpapers` and downloads XML 
- sections papers using `ami-section`
- gets the PMCIDs, Abstracts and Keywords from the metadata of individual papers
- globs and parses the XML to get the section of your interest (result, method, etc.)
- extracts key phrases from that section using YAKE
- recognizes entities (like organism, chemical, gene, gene product, and so on) using scispacy
- splits the section paragraphs of indivdiual papers into a list of words and looks for a particular string ('TPS' or 'citrus' for example) in the words and retreives them
- matches against a given set of phrases (like terpene synthase, terponoids, or species name) and retrieves them for each para
- outputs all the analysis as a `.csv` for interprations and conclusions. A typical output is available [here](https://github.com/petermr/crops/blob/main/metadata_analysis/filtered_for_tps_citrus_results_sec.csv). Since it's too large of a file for GitHub to display on GUI, you would have to download it to view. 

Some elements including the data structure is inspired by [`docanalysis`](https://github.com/petermr/crops/blob/main/metadata_analysis/metadata_analysis.py) code which was mostly written by [Ayush](https://github.com/ayush4921).

The script has a potential to widen into other genes of other orgnanisms, or mine for any information (similar to gene names) of your interest.

## Interested in running it yourself?
- I recommend you set up a virtual environment. Scispacy gives you trouble otherwise. If you are on Windows, check out this [video tutorial](https://www.youtube.com/watch?v=APOPm01BVrk&t) to set up `venv`.
- There's a `requirements.txt` mentioning all the dependencies that you can install by running `pip install -r requirements.txt` from working directory
- [`metadata_analysis`](https://github.com/petermr/crops/blob/main/metadata_analysis/metadata_analysis.py) is the main script. I will document what each funciton does, if I get time

Any feedback would be really appreciated!

