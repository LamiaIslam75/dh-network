# Division of our notebooks in OERs + Formats

Different Formats:
* Input without interaction of the user: Text / Video
* Input with user interaction: Notebooks / User defines path (e.g. which post correction to look at) 
* Tests: 
 * Quizzes (multiple choice questions, Binary eihter/or questions) 
 * Sorting (e.g. given this setup, what steps need to be taken in which order / sort the choice of tools accordingly),  
 * Ranking (e.g. rank data formats in terms of their automatic processability)

## Chapter 0. Introduction: Operationalization of the research question - How to examine media waves: Video 
 * Where are we starting from? (newspaper articles in PDF / jpg format)
 * Where do we want to end up? (wikipedia like plot on the newspaper coverage on the Spanish flu)

## Chapter 1: Corpus Collection 
1. Text as digital object – formats: pdf / jpg: Text / Video 
2. Metadata (conceptual introduction)?: Text / Video
 * What fields do we need? 
 * What fields are there, what fields should be added?
 * Format 

## Chapter 2: Corpus Preparation
3. What is OCR?
  * What is OCR?: Text / Video
  * OCR services: Text / Table  
	  * What libraries are they?
	  * What are we using and why?
4. Application of OCR: Notebook (with Text)
  * What does input data look like?
  * How is it applied?
  * What does the output look like?
5. Quality of OCR : Text / Video & Notebook 
  * How to compare output?
  * Producing gold-standard data manually 
  * measurements: accuracy, precision, recall, F1
## Chapter 3: Post-Correction of OCR
6. Post-Correction: Text / Video
  * Why and when do we need it?
  * What different methods are there? Manual, Rule-Based, LLM-based
7. The concept of rule-based Post-Correction: Text / Video
  * Typical OCR mistakes are introduced 
  * RegEx is introduced: Point to external resource (Video / Text / Tutorial) 
8. Executing rule-based Post Correction: Notebook
  * Compilation of typical errors by students
  * Formulate find / replace or regex pattern for correction 
9. Conceptual Introduction to Post-Correction with LLMs: Text / Video
  * Abstract explanation: What are LLMs, why can they help us?
  * What LLMs are available?
  * Why do we use X?
  * How we use X
  * Option: Input into Notebook OR directly save as txt file
10. LLM-Based Post-Correction: Notebook 
  * Users input the output of LLMs
  * OR: Users look at corrected txt-files and can post-correct them  

## Chapter 4: Corpus Processing: From strings to sentences and tokens (NLP) 
14. More to 1.: What do plain texts look like?: Text & Notebook
  * Texts as lists of characters
15. Introduction: NLP as a method to 'semantizise' texts: Text / Video
  * What is NLP
  * Methods of NLP: Text & Notebook
	  * Tokenization (also: lazy tokenization) 
	  * Lemmatization
	  * sentence splitting
	  * PoS-Tagging
  * Which libraries are available?
  * What tasks can be carried out by the libraries?
16. NLP with spacy: Text
 * Quality of spacy 
 * How to compare output?
 * measurements: accuracy, precision, recall, F1 
 * How to asssess the results of spacy
   * Language domain
   * historicity of language
17. NLP on our research objects (Notebook)   
18. Annotated Text format (Text as a table): Text / Video

## Chapter 5: Corpus Analysis 
21a. How to get from a table like text to media waves? (conceptual introduction to Operationalization): Video
 * Basis for analysis: Notebook
   * Lemmata
   * Metadata: year, newspaper
### Diachronic Analysis of semantic fields
21b: Line plot: Text / Video
  * analysing word frequencies over time 
  * analysing groups of words over time (conceptual: group of words as semantic field / topic?)
22: KWIC search of words: Notebook
  * How to get to groups of words?
  * Searching by lemma
  * Investigations of the context of Grippe 
  * (Building more word groups)
23. Analysis 1 – Talking about the flu: Text & Notebook
  * absolute frequency: of one word / group of words
  * relative frequency: "" 
  * discussion of results
### Diachronic Analysis by newspaper
24. Analysis 2 – Who is talking about the flu: Notebook
 * relative frequency
 * newspaper specific -> parameterization
## Chapter 6: Wrap Up
26. Final Discussion: Video
  * Comparison of Analysis results with high quality data and data created in the case study

## Questions & Answers
* It is not important how tesseract and spacy do it under the hood? –> only conceptual understanding
* Is KWIC obvious or needs conceptual input?
* How to handle cycles? Going from KWIC to line plot to KWIC and so on
  * Als Übung: Guck dir den Kontext an, welche Wörter passen noch? 
  * noch als einzelnes Übungsnotebook? 
