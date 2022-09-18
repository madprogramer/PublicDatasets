# PublicDatasets
Research Project Repo on How Datasets are Cited @ PURRlab, [ITU Copenhagen](http://en.itu.dk/)

## At a glance
Machine learning challenges hosted on platforms such as Kaggle, grand-challenge.org, or CodaLab have attracted a lot of attention, both from academia and industry researchers. Challenge designs vary widely, including what type of data is available, how the algorithms are evaluated, and the rewards for the winners. In medical imaging, there is some evidence that challenges might be creating a shift in attention to different diseases, for example, there is a disproportionate increase in papers on lung cancer after the 2016 Kaggle challenge on the subject.

However, it is actually non-trivial to observe the impact these datasets have on research and technology. There are no well-defined conventions for citing most public datasets, which often come from outside of academic journals. The overall goal of this project is to understand how we can relate research to datasets they either use or are inspired by.

## Log

### 18-09-2022 : On Identifiers
Last week I collected oral papers from MIDL 2018* on [openreview.net](https://openreview.net/group?id=MIDL.amsterdam/2018/Conference). This was a conference that took place right after [Data Science Bowl '17](https://www.kaggle.com/c/data-science-bowl-2017) so it seemed like a good source to observe immediate feedback.

\* (Medical Imaging with Deep Learning)

I couldn't help but notice that many of these papers were missing their [DOI](https://doi.org/). A minority of authors had access to [arXiv](https://arxiv.org/) so that gave them an easy DOI for preprints. Other authors had to wait between 1 or 3 years to get published in some journal, usually owned by Elsevier, to receive a proper DOI. As I myself am on the fence of whether or not I want to continue onto a PhD, this was a nice reminder that you should never expect immediate recognition for your work. Even when deserved, it has to be earned.

For example, let's take the paper: [_Recurrent Inference Machines for Accelerated MRI Reconstruction_](https://openreview.net/forum?id=rJD6Xgnoz) by Lønning et al. This version of the paper from 2018 has no DOI. But it does have some other identifiers. It came out of the [Spinoza Centre for Neuroimaging](https://pure.knaw.nl/portal/en/organisations/spinoza-centre-for-neuroimaging) in the Netherlands, a country which has [several national identifers](https://www.narcis.nl/about/Language/en). Thus it is possible to identify the paper by [NBN or Handle](https://www.narcis.nl/publication/RecordID/oai:pure.knaw.nl:publications%2F1b3afd87-4c94-4766-848f-b1f2bd154933). Another version of _The Recurrent Inference Machines_ paper did eventually receive a DOI, titled _Recurrent inference machines for reconstructing heterogeneous MRI data_ in the journal _Medical Image Analysis_. As you can imagine, this did not happen until 2019 and _Medical Image Analysis_ is also published by Elsevier.

But of course, I only need identifers for future reference, the papers themselves are from an open-access conference after all. Unfortunately, `openreview.net` is no `wikipedia.org`, it does not usher the same level of trust and permanence. Therefore I feel identifying papers by link alone would be a liability for reproducability.

For the time being, I have only marked those papers whose identifiers I was not able to find as `n/a`. I must admit that I find it quite funny how while I am trying to examine the negotiation between academia and the web, that I also have to put-up with the internal struggles within Academia itself as well. Now I'm left wondering if I should stick to listing DOI-only or bite the bullet and have links as an alternative identifier. 

Logging off, until next time (\^_^/).

### The Story so Far:
My initial approach has been to work backwards: To first collect literature and _then to scan_ for mentions of corresponding datasets. This is solely motivated by the fact that there are a lot more tools to query literature.

The first dataset of interest comes from the [Kaggle Data Science Bowl '17](https://www.kaggle.com/c/data-science-bowl-2017). This was a lung-cancer tissue detection challenge with annotated data provided by The [National Lung Screening Trial](https://www.cancer.gov/types/lung/research/nlst), [Copenhagen University Hospital](https://universitetshospitalet.ku.dk/english/about/) and others. Arguably, the challenge and corresponding dataset inspired a new interest in lung cancer research; see [(Varoquaux & Cheplygina, 2022)](https://arxiv.org/pdf/2103.10292.pdf).