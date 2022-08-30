# st_xsum
Custom XSum visualization using streamlight

# Steps to run
1. Create conda environment 'summviz' and activate
2. pip install -r requirements.txt
3. python -m spacy download en_core_web_lg
4. python preprocessing.py --workflow --dataset_jsonl xsum_hallu_demo.jsonl --processed_dataset_path xsum_hallu_demo.cache
5. streamlit run summvis.py -- --path xsum_hallu_demo.cache
