# PublicDatasets
Research Project Repo on How Datasets are Cited @ PURRlab, [ITU Copenhagen](http://en.itu.dk/)

Install with `pip3  install -r requirements.txt`.

This project allows you to build datasets of dataset mentions from papers published in https://proceedings.mlr.press/.

Background:

As part of my research project, I analyzed dataset mentions in CHIL 2022. You can refer to my report_logs or see [the presentation](
https://github.com/madprogramer/PublicDatasets/blob/main/report_logs/Towards%20Understanding%20The%20Hidden%20Popularity%20of%20Machine%20Learning%20Datasets_Slides.pptx) for a tl;dr.

Code:  

* ArticleOrganizer.ipynb : Runs first, selects target venues and downloads their contents locally. Generates `ResearchPapers.csv`.
* ArticleAnalayzer.ipynb : Runs second, requires some configuration to know where in the text to look for research paper mentions. Generates `DatasetMentions_Unprocessed.csv`, a table which may be further annotated to include `Dataset Identifier` and `Access`.
* ArticleVisualizer.ipynb : Run after cleaning and annotating your `unprocessed` file to generate visualizations.

Data:

* data/ResearchPapers.csv : A table of research papers which have been downloaded and their respective venues.
* data/DatasetMentions_Unprocessed.csv : A table of research papers which have been downloaded and their respective venues. Dataset mentions are sorted by the paper and venue they occur in. The `Mention Style` and `Mention` column indicate the type of mention and how it occurs in the text. The `Notes` column is used to indicate the original context so that an annotator may validate and make corrections if necessary.
* data/DatasetMentions_Processed.csv : A table of which has been manually annotated over `DatasetMentions_Unprocessed`. Redudant columns were merged and footnotes were replaced with URLs instead of numbers. The example used in this repository introduces the `Dataset Identifier` and `Access` columns for the `ArticleVisualizer.ipynb` visualizer.
