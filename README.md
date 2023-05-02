# Extraction of string-citations in court data

Workshop:
[Extracting heterogeneous reference data](https://mpilhlt.github.io/reference-extraction/workshop-2023/programme/)

MPI Frankfurt 2023

Kilian Lüders & Bent Stohlmann
Contact: kilian.lueders@hu-berlin.de

*In this repo, we provide code and sample data to demonstrate our approach to work with GFCC references.* -> *tutorial.ipynb*

(In case there are compatibility problems: *bverfge-env.yaml* provides the Conda environment.)


# Abstract
We are currently working on a project of extracting references in the decisions of the German Federal Constitutional Court (GFCC). In particular, we are interested in the self-referencing of the court.

So-called citation networks for courts are an established use case of reference data. Especially concerning the United States Supreme Court (USSC), there is a long history of studies regarding its references to prior decisions (e.g. Fowler et al. 2007). Also, there is some recent work on the network of references between decisions of the Court of Justice for the European Union (CJEU) (e.g. Šadl and Olsen 2017).

Up until now, there has been little work regarding the self-references of the GFCC (although recently there have been first studies Ighreiz et al. 2020; Coupette 2019). Presenting our work on self-references of the GFCC would fit within the conception of the workshop in two ways.

Firstly, networks of court self-citation are a current use case in which the extracting of heterogeneous reference data arises. With the availability of research into large data sets of court decisions being a relatively young phenomenon, there are various promising research questions the answer to which relies on the extracting of such data. On the one hand, we could learn about differences in style between certain types of decisions or concerning their relevance (issue of centrality). On the other hand, we could learn more about the role prior decisions play in a court’s justification of its decisions (issue of normativity).

Secondly, we can present a working extraction framework approaching the issue of extracting reference data of the GFCC regarding its prior decisions. While there is prior work here (see above) our solution is the first to provide a way to extract string citations. String citations are a prominent phenomenon in the way the GFCC refers to its prior case law (Jestaedt 2010, 151). In legal literature, it is also discussed as an important feature of the court’s argumentation (Holzleithner and Mayer-Schönberger 2000, 338). String citations link references to multiple prior decisions together (regarding string citations in the CJEUs case law see Jacob 2014, 100). This linkage makes it challenging to extract all the reference information. Our main work was to find such sequences of references within decisions and then store them as a unit of information.

For extracting the references from the text of the court decisions, we use a classical rule-based approach (regex patterns) because the court makes its self-references comparatively uniformly. To handle the data, we programmed an object-oriented solution that is customized to our needs: There is a class “Verweis” (reference) that is equipped with attributes that are required for citations in the “BVerfGE” style. In addition, there is a class “Verweiskette” (string-citation), which ultimately consists of an ordered list of objects of the class “Verweis”. Both classes provide methods to output the information for different purposes. From a programming perspective, this is a straightforward application of a fundamental paradigm of computer science. Although it is very specific to a problem, it can be easily adapted and is characterized in particular by very good scalability. At the same time, string citations in that particular form are a very specific reference type with limited comparability to established reference types in other contexts.

For this task, we used a corpus consisting of all decisions of the GFCC’s senates. An earlier version of this corpus containing linguistic annotation data as well as metadata information was previously made available as part of our research project (LLCon) (Möllers, Shadrova, and Wendel 2021).

## Literatur
- Black/Spriggs, The Citation and Depreciation of U.S. Supreme Court Precedent, Journal of Empirical Legal Studies 2013, 325.
- Brodocz/Schäller, Selbstreferenzielles Entscheiden und institutionelle Eigengeschichte – Eine quantitative Analyse zur Rechtsprechung am Bundesverfassungsgericht, Dresdner Beiträge zur Politischen Theorie und Ideengeschichte, Nr. 3/2005.
- Coupette, Juristische Netzwerkforschung 2019.
- Derlén/Lindholm, Peek-A-Boo, It’s a Case Law System! Comparing the European Court of Justice and the United States Supreme Court from a Network Perspective, German Law Journal 2017, 647.
- Fowler u. a., Network Analysis and the Law: Measuring the Legal Importance of Precedents at the U.S. Supreme Court, Political Analyis 2007, 324.
- Granger/Pérez, Jupyter: Thinking and Storytelling With Code and Data, Computing in Science & Engineering 2021 (23/2), 7-14. DOI:10.1109/MCSE.2021.3059263.
- Harris/Millman/van der Walt et al., Array programming with NumPy, Nature 585 (2020), 357–362. DOI:10.1038/s41586-020-2649-2
- Holzleithner/Mayer-Schönberger, Das Zitat als grundloser Grund rechtlicher Legitimität, in: Feldner/Forgó (eds.), Norm und Entscheidung – Prolegomena zu einer Theorie des Falls, 2000, 318.
- Ighreiz u. a., Karlsruher Kanones? Selbst- und Fremdkanonisierung der Rechtsprechung des Bundesverfassungsgerichts, Archiv öffentlichen Rechts 2020, 537.
- Jacob, Precedent and Case-Based Reasoning in the European Court of Justice – Unfinished Business 2014.
- Jesteadt, Autorität und Zitat – Anmerkungen zur Zitierpraxis des Bundesverfassungsgerichts, in: Jacob/Mayer, Ethik des Zitierens 2010, 141.
- Jiang, Network research in law: current scholarship in review, Humanities & Social Sciences Reviews 2019, 528.
- McKinney, Data structures for statistical computing in python, Proceedings of the 9th Python in Science Conference, Volume 445, 2010.
- Möllers/Shadrova/Wendel, BVerfGE-Korpus (1.0) [Data set], 2021, available at: https://zenodo.org/record/4551408.
- pandas development team, pandas-dev/pandas: Pandas (v2.0.0) 2023. DOI:10.5281/zenodo.7794821.
- Python Software Foundation. Python Language Reference, version 3.10. Available at http://www.python.org
- Richardson, Beautiful soup, version 4.12.2 (2023). Available at https://www.crummy.com/software/BeautifulSoup/.
- Šadl/Olsen, Can Quantitative Methods Complement Doctrinal Legal Studies? Using Citation Network and Corpus Linguistic Analysis to Understand International Courts, Leiden Journal of International Law 2017, 327.
- Wendel, Metadaten zu Entscheidungen des Bundesverfassungsgerichts (2.6.1) [Data set], 2023, available at: https://doi.org/10.5281/zenodo.7664631.
- Whalen, Legal Networks: The promises and challenges of legal network analysis, Michigan State Law Review 2016, 539.