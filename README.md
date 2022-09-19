# PublicDatasets
Research Project Repo on How Datasets are Cited @ PURRlab, [ITU Copenhagen](http://en.itu.dk/)

## At a glance
Machine learning challenges hosted on platforms such as Kaggle, grand-challenge.org, or CodaLab have attracted a lot of attention, both from academia and industry researchers. Challenge designs vary widely, including what type of data is available, how the algorithms are evaluated, and the rewards for the winners. In medical imaging, there is some evidence that challenges might be creating a shift in attention to different diseases, for example, there is a disproportionate increase in papers on lung cancer after the 2016 Kaggle challenge on the subject.

However, it is actually non-trivial to observe the impact these datasets have on research and technology. There are no well-defined conventions for citing most public datasets, which often come from outside of academic journals. The overall goal of this project is to understand how we can relate research to datasets they either use or are inspired by.

## Log

### 19-09-2022 : Citation vs. Attribution

As a refresher, the first public dataset I'm searching for are mentions of the Lung Image dataset from [Kaggle Data Science Bowl '17](https://www.kaggle.com/c/data-science-bowl-2017). To that end, I'm querying for the terms `Data Science Bowl 2017`, `Nodule`, `Lung`, `Lung Tissue` and `Lung Imaging` in either the body, keywords or title of my collected papers. Intuitively this sounded like a good idea; until, of course, some things went wrong.

For example, [_MILD-Net: Minimal information loss dilated network for gland instance segmentation in colon histology images (Graham et al., 2018)_](https://doi.org/10.1016/j.media.2018.12.001) and [_Evaluating Reinforcement Learning Agents for Anatomical Landmark Detection (Alansary et al., 2018)_](https://doi.org/10.1016/j.media.2019.02.007) cite work on `Lung Cancer` and `Lymph Node` detection in related work, but with no explicit mention in the body. They are presented as applications of machine learning, or as one paper put it: `computerized techniques`. To quote from the _MILD-Net_ paper which drops a lengthy citation in the middle of the introduction:

> 1. Introduction
> ...
> Computerized techniques play a significant role in automated digitalized histology image analysis, with applications to various tasks including but limited to nuclei detection and segmentation (Graham, Rajpoot, 2018, Chen, Qi, Yu, Dou, Qin, Heng, 2017, Sirinukunwattana, Raza, Tsang, Snead, Cree, Rajpoot, 2016), mitosis detection (Cireşan, Giusti, Gambardella, Schmidhuber, 2013, Chen, Dou, Wang, Qin, Heng, et al., 2016, Veta, Van Diest, Willems, Wang, Madabhushi, Cruz-Roa, Gonzalez, Larsen, Vestergaard, Dahl, et al., 2015, Albarqouni, Baur, Achilles, Belagiannis, Demirci, Navab, 2016), tumor segmentation (Qaiser et al., 2017), image retrieval (Sapkota, Shi, Xing, Yang, 2018, Shi, Xing, Xu, Xie, Su, Yang, 2017), cancer type classification (Graham, Shaban, Qaiser, Khurram, Rajpoot, 2018, Kong, Wang, Li, Song, Zhang, 2017, Bejnordi, Veta, Van Diest, Van Ginneken, Karssemeijer, Litjens, Van Der Laak, Hermsen, Manson, Balkenhol, et al., 2017, Lin, Chen, Dou, Wang, Qin, Heng, 2018, Qaiser, Mukherjee, Reddy Pb, Munugoti, Tallam, Pitkäaho, Lehtimäki, Naughton, Berseth, Pedraza, et al., 2018), etc.
> ...
> 
> Graham, Shaban, Qaiser, Khurram, Rajpoot, 2018
S. Graham, M. Shaban, T. Qaiser, S.A. Khurram, N. Rajpoot
Classification of lung cancer histology images using patch-level summary statistics
Medical Imaging 2018: Digital Pathology, 10581, International Society for Optics and Photonics (2018), p. 1058119

Another paper, with some shared authors, titled [_Attention U-Net: Learning Where to Look for the Pancreas (Oktay et ak., 2018)_](https://doi.org/10.48550/arXiv.1804.03999) is a lot more explicit in connecting `lung`-related medical imaging tasks to the paper:

> 1. Introduction
> Automated medical image segmentation has been extensively studied in the image analysis community
due to the fact that manual, dense labelling of large amounts of medical images is a tedious and
error-prone task. Accurate and reliable solutions are desired to increase clinical work flow efficiency
and support decision making through fast and automatic extraction of quantitative measurements.
With the advent of convolutional neural networks (CNNs), near-radiologist level performance can
be achieved in automated medical image analysis tasks including cardiac MR segmentation [3] and
cancerous lung nodule detection [17].
> ...
>
> [17] Liao, F., Liang, M., Li, Z., Hu, X., Song, S.: Evaluate the malignancy of pulmonary nodules
using the 3D deep leaky noisy-or network. arXiv preprint arXiv:1711.08324 (2017)

On my part, I was only able to mark the _Attention U-Net_ paper as relating to `lung`s and `nodule` detection, even if it may be argued that the _MILD-Net_ and _Reinforcement Learning Agents_ papers also connected to this work. None of these are papers on lung imaging, but only derive some influence therefrom. Thus there were no experiments involving lung images here, at all.

Moving onto papers which **do** actually deal with lung imaging, even then it's not always clear at what granularity the work is relevant. The paper [_Temporal Interpolation via Motion Field Prediction (Zhang et al., 2018)_](https://doi.org/10.48550/arXiv.1804.04440) refers to `Lung Tissue` as `Lung Structure` and so I discovered that my precise keyword-search for `Lung Tissue` was missing something which could be considered relevant. Perhaps, I ought to refine my method to be able to catch synonyms or similar terms.

We tend to hold citation in a higher regard to attribution, that is to say the precise reference to related works is considered more valuable than the concrete explanation of the connection to said related works. While this practice has the advantage of making it easier to find the original work, it doesn't tell where and what for. An informal quote exchanged between colleagues can, surprisingly, reveal a whole lot more.

These are all things for future authors to consdider, but as to me I'm going to need a more flexible search rule if I intend to get anywhere.

Logging off, until next time \(^_^)/.


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