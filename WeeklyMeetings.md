
# Ahmet's Weekly Meeting Notes

* [1 December 2022](#date-1-december-2022)

* [28 November 2022](#date-28-november-2022)

* [17 November 2022](#date-17-november-2022)

* [9 November 2022](#date-9-november-2022)

* [31 October 2022](#date-31-october-2022)

* [6 October 2022](#date-29-september-2022)

* [29 September 2022](#date-29-september-2022)

* [22 September 2022](#date-22-september-2022)

* [1 September 2022](#date-1-september-2022)

* `Todo: Meetings Before?`

* [Template](#template-date-dd-month-yyyy)

### Date: 1 December 2022

#### Who did you help this week?

* Gave some motivation to Catthrine and Trine. 

#### What helped you this week?

* A reminder from my boss at work that sometimes the [Minimum Viable Product](https://www.agilealliance.org/glossary/mvp/) is the best product.

#### What did you achieve?

* I discovered a serious issue in my pipeline

<img width="843" alt="image" src="https://user-images.githubusercontent.com/3719664/205052759-7cbbe530-287b-4377-94a6-655bd30a71c4.png">

* Some articles were not parsing.

<img width="660" alt="image" src="https://user-images.githubusercontent.com/3719664/205053175-902bed4d-abb9-4e2d-901f-cad9b7cd3e97.png">

* It turns out the text was being jumbled.

<img width="747" alt="image" src="https://user-images.githubusercontent.com/3719664/205053083-42bd4326-a5d1-4313-8411-24064a247edd.png">

#### What did you struggle with?

* Avoiding manual annotation.

#### What would you like to work on next week?

* Solution: Incorporate manual annotation into methodology.
  * The goal of automation now is to make annotation easier, however, anyone repeating or extending my work will also need to do some manual work after.
  * The last step of automation will now produce **excerpts** which contain the references to datasets. It is now the responsibility of the annotator to extract the final details into the dataset they produce.

![image](https://user-images.githubusercontent.com/3719664/205053897-480aec80-4173-408a-8834-82d9e16e557d.png)


#### Where do you need help from Veronika?

* How can I contact you next week if I need to ask anything?

### Date: 28 November 2022

#### Who did you help this week?

* No one :|

#### What helped you this week?

* Going over [past notes on Notion](https://www.notion.so/vcheplygina/PublicDatasets-Ahmet-efe0dbcb1740488a86878f48196f051c) has been helpful. I was much better of keeping track of everything when I first started the project and that has given me ample material for the report.

#### What did you achieve?

* [Progress on report](https://www.overleaf.com/read/wnkpgqnykcty).

#### What did you struggle with?

* Time Management: Part-time work and my other research project have been quite draining.
* Trying to minimize manual annotation.

#### What would you like to work on next week?

* Results:
  * Research obervations have given us new problems to examine.
    * Bibliometric Exclusion: The consequences of Datasets being used even when not cited in the bibliography.
    * Broken Links: Frequency of ML Challenge Web Addresses being noted incorrectly or being unreachable.

#### Where do you need help from Veronika?

* How do we demonstrate under-representation:
  * Statistical power? 
  * F.x. the Power Inequality Effect definition from the [The glass ceiling in NLP](https://aclanthology.org/D18-1301.pdf) paper.

* Does it make sense to include raw PDFs or .txt files in the dataset?
  * These are retrievable my script, anyway.

### Date: 17 November 2022

#### Who did you help this week?

* No one :|

#### What helped you this week?

* [Christina's Thesis Notes](https://github.com/christinekaarde/MICCAI-review-thesis/tree/main/04-analysis) have been helpful figuring out what to do next.

#### What did you achieve?

* Data Schema for Datasets in Research Papers: 
* <img width="1128" alt="image" src="https://user-images.githubusercontent.com/3719664/202332452-69c97c53-3ca4-4a25-9156-303c2b600028.png">

* Can fully automate:
  *  Venue
  *  Title
  *  Dataset Origin (given URL)
* Can partially automate (**on keyword matches. F.x. Kaggle.**)
  *  Citation Category (Footnote, Journal Publication or URL)
  *  Access (Public or Private)
  *  Bibliography Mentions
*  Not so easy to automate:
  * Dataset Identifier
    *  Multiple references, sometimes full name sometimes abbreviated.
    *  f.x. Usiigaci is not trivially associable with the title `Nucleus segmentation across imaging experiments: the 2018 Data Science Bowl`.
  * Notes
    * When keyword match isn't present, annotation requires further context.

#### What did you struggle with?

* No matter what I do, some manual annotation is needed.
  * This hurts the scalability of my results. 
* Behind on plotting, but I expect to catch up next week.
* I realized it might be a bit overkill to include **every** dataset used in a research paper.
  * If I only include challenge datasets, I will only be able to compare them amongst each other:
    * Footnotes vs. Bibliographic Citations. Broken, Rotten and Active Links.
  * But if I should exclude any datasets, I don't know which ones to exclude.
    * Can compare dataset hosts (GitHub vs. Institutional), frequency of challenge datasets against baseline.

#### What would you like to work on next week?

* Results, results, results!
* If I complete the pipeline on the automatable data,
  * then I can manually fill in the remaining fields and update figures in future weeks.
  * This would require me to churn most of the report within the next 2 weeks.

#### Where do you need help from Veronika?

* What should my inclusion/exclusion criteria be on datasets from our collected research papers?

* My deadline is December 15, but I am starting to worry if I might need an extension.
 * What are my options? Scaling down my scope or extending my deadline?

### Date: 9 November 2022

#### Who did you help this week?

* No one :|

#### What helped you this week?

* Reading past notes.

#### What did you achieve?

* Some notes on challenge dataset hunting:
  * In papers comparing multiple datasets there is often a dedicated section listing all datasets.
  * Appendices matter! There may be additional datasets only mentioned after the paper.

* Challenge datasets are presented in one of three ways:
 * The X competition
   * Ex. _moco-cxr performance on the `chexpert` competition task pathologies._
 * The X chalenge
   * Ex. _the 2019 `fastmri` challenge_
   * as opposed to _The goal of the conference is to foster excellent research that addresses the unique `challenge`s and opportunities_
 * URL identifier
   * Ex. https://www.kaggle.com/c/rsna-pneumonia-detection-challenge or https://promise12.grand-challenge.org

#### What did you struggle with?

* Analysis Paralysis:
  * I'm not sure what I want to annotate, and with what tool
  * How to scale it to 128 PDFs?
* Comparing non-challenge datasets to challenge datasets
  * Annotation seems infeasible.

#### What would you like to work on next week?

* Improving biblography checker.
* Retrieving contest identifier by pattern-matching

#### Where do you need help from Veronika?

* Any other querying ideas?

* Good practices for annotation?
* What should I tag and why?
 * My hypothesis is that "Challenge datasets are under-represented in bibliographies (than there actually are)" 

#### Any other topics

* Forgot to add checks on Title :_)

### Date: 31 October 2022

#### Who did you help this week?

* No one :|

#### What helped you this week?

* I did attend the Digital Tech Summit though, which I'd love to talk about this week.

* Earlier this month Bethany helped me with some suggestions. I also gave her some ideas, but they came a bit late into her project. 

#### What did you achieve?

* I realized that it's a good idea to check for keywords **in bibliography** and before **bibliography**: 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7a8f7fae-f2ed-44be-a1d2-c6adc32a3247/Untitled.png)
![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/77d5d199-4139-41d3-b3e1-207bbf95a318/Untitled.png)

* I now actually have an objective way to demonstrate representation of online datasets (through bibliography)
  * Now do I build a hypothesis that this is a under-representation?

* Misc. refactoring
  * Main dataset is venues/titles only
   * Will later enable output for alternative match rules. 

#### What did you struggle with?

* The context-sensitivity of the word "challenge" makes it difficult as a keyword:
  * "Challenges in Machine Learning" vs. "Machine Learning Challenges" 

#### What would you like to work on next week?

* Improving biblography checker.
* Querying even more venues!
* Can now do some basic quantative.

#### Where do you need help from Veronika?

* Any other querying ideas?

* What are some meaningful comparisons?
  * `Kaggle` mentioned in body vs. Bibliography?
  * `Competition` mentioned in title + body vs. Bibliography?
  * Number of times `competition` mentioned in title + body vs. Bibliography

* Will have to do some tagging (i.e. if name is Data Science Bowl instead of Kaggle)
  * Workaround ideas? 

#### Any other topics

* Forgot to add checks on Title :_)

### Date: 6 October 2022

#### Who did you help this week?

* Just sharing some ideas with the `MentalHealth` project members over MS Teams.

#### What helped you this week?

* Bethany's session on Surveys and Zotero from last week.
* [Scrapy docs](https://docs.scrapy.org/) for webcrawling.

#### What did you achieve?

* Coded a working pipeline!
* Producing a new dataset checking name/keyword mentions on `Data Science Bowl 2017` in MIDL 2021 papers.

#### What did you struggle with?

- DOIs are missing. They were missing from the proceedings and I don’t yet have a strategy to scan for them.
- I’m not filtering, for example, the preface of the proceedings. It was also downloaded and saved as `Proceedings.pdf` as part of the dataset.
- Match frequency isn’t taken into consideration. One match is just as good as 100 in this scheme.
  - Also, I have no way to check for homographic false-positives. Hence the `DSB` 2017 vs. 2018 confusion.

#### What would you like to work on next week?

As far as future work goes, searching for `kaggle` was the most revealing thing I came up with. When we have the collection of publications from a particular venue (or set of venues) we can find references to datasets which are missed in most relevance-based indexing systems.

Then perhaps, instead of focussing on `DSB` alone we might try querying the word `kaggle` to extract a family of interrelated datasets across publications.

#### Where do you need help from Veronika?

* Should we increase the number of venues?
  * Which venues?
  * What years?
* Is the `kaggle`, `competition` querying for discovery a good idea?

#### Any other topics

I am also going to conference next week (Belgium from the 12-14th).

### Date: 29 September 2022

#### Who did you help this week?

It's not much but Amelia & Olivia seem to be interested in the (creative, critical & feminism) methods of ETHOS lab, which I told them I joined recently.

#### What helped you this week?

* The [pdfminer.six](https://github.com/pdfminer/pdfminer.six) project gave me a decent way to bulk-extract text from PDFs.
* Thu Vu's https://github.com/thu-vu92/the_witcher_network project was some nice inspo.

#### What did you achieve?

* Devised basic pipeline for data collection.
  * Still need to finish the code, though :)
![PublicDatasetsv1](https://user-images.githubusercontent.com/3719664/192954418-a336e888-0d1d-474f-b187-a141ff53fea3.png)

#### What did you struggle with?

* Text extraction from PDFs
  * My previous tool, https://github.com/kingaling/pydf2json was outdated and too verbose.
  * Recovered thanks to pdfminer.six.

#### What would you like to work on next week?

* Coding :)
* Determining some nice keywords.
  * No quantitive analysis yet, only direct inspection. Although, maybe relevant in the future.

#### Where do you need help from Veronika?

* Nothing for this week :)

#### Any other topics

Maybe should meet with Bethany some time next week to exchange ideas.


### Date: 22 September 2022

#### Who did you help this week?

n/a

#### What helped you this week?

Some resources on semantic search for flexible keyword queries:
* Hugging Face: https://www.youtube.com/watch?v=OATCgQtNX2o
* Amir Shamsi on Gensim: https://stackoverflow.com/a/71828372/2089784
* Trey Grainger on Data Philosophy and Solr: https://www.youtube.com/watch?v=4fMZnunTRF8

#### What did you achieve?

* [Collected MIDl 2018 papers](https://github.com/madprogramer/PublicDatasets/blob/main/data/ResearchPapers.csv)
  * Annotated for DOI, if available
  * Annotated for keywrod matches

#### What did you struggle with?

* Did not find any matches for `Data Science Bowl 2017`.
* Precise keyword searches can miss, false negative matches

#### What would you like to work on next week?

* Figure out PDF extraction pipeline. Searching for datasets in conference papers is like searching for a needle in a haystack so we need to be able to process more PDFs faster.

#### Where do you need help from Veronika?

* Is it a good idea to stick to MIDL (future years?)
  * MICCAI?
* Try different keywords maybe

#### Any other topics

This space is yours to add to as needed.










### Date: [Template]

#### Who did you help this week?

Replace this text with a one/two sentence description of who you helped this week and how.


#### What helped you this week?

Replace this text with a one/two sentence description of what helped you this week and how.

#### What did you achieve?

* Replace this text with a bullet point list of what you achieved this week.
* It's ok if your list is only one bullet point long!

#### What did you struggle with?

* Replace this text with a bullet point list of where you struggled this week.
* It's ok if your list is only one bullet point long!

#### What would you like to work on next week?

* Replace this text with a bullet point list of what you would like to work on next week.
* It's ok if your list is only one bullet point long!
* Try to estimate how long each task will take.

#### Where do you need help from Veronika?

* Replace this text with a bullet point list of what you need help from Veronica on.
* It's ok if your list is only one bullet point long!
* Try to estimate how long each task will take.

#### Any other topics

This space is yours to add to as needed.


