#!/usr/bin/env python 

from pathlib import Path
from argparse import ArgumentParser

import spacy
import pandas as pd

# processing 162 M, so pipeline is read -> annotate -> write for every text
def read_annotate_write(corpus_dir: Path, nlp, disable_components:list[str], output_dir:Path, suffix:str) -> None:
    for filepath in corpus_dir.iterdir():
        if filepath.is_file():
            text = filepath.read_text()
            doc = nlp(text, disable=disable_components)
            annotated_text = {}
            annotated_text['Token'] = [tok.text for tok in doc]
            annotated_text['Lemma'] = [tok.lemma_ for tok in doc]
            output_path = output_dir / filepath.with_suffix(suffix).name
            pd.DataFrame(annotated_text).to_csv(output_path, index=False)

def _parse_args():
    parser = ArgumentParser(description="Annotate txt files of a given directory with spacy for PoS and Lemma")
    parser.add_argument("corpus_dir", type=Path, help="Path to corpus directory")
    parser.add_argument("--output_dir", type=Path, help="Path to output directory", default=Path().cwd())
    parser.add_argument("--spacy_model", help="name of the language specific spacy model", default="de_core_news_sm")
    parser.add_argument("--output_suffix", help="Define the file suffix of the output files", default=".tsv")
    return parser.parse_args()

def main():
    args = _parse_args()

    nlp = spacy.load(args.spacy_model, exclude=['parser', 'ner'])
    
    # followed this issue: https://github.com/explosion/spaCy/issues/6498
    disable_components = ["parser", "ner"]

    read_annotate_write(args.corpus_dir, nlp, disable_components, args.output_dir, args.output_suffix)

if __name__ == "__main__":
    main()
