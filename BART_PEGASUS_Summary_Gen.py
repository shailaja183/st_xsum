import argparse
import json
import os

import torch
from tqdm import tqdm
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

BATCH_SIZE = 8
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

BART_XSUM_CHECKPOINT = 'facebook/bart-large-xsum'
PEGASUS_XSUM_CHECKPOINT = 'google/pegasus-xsum'

MODEL_CHECKPOINTS = {
    'pegasus-xsum': PEGASUS_XSUM_CHECKPOINT,
    'bart-xsum': BART_XSUM_CHECKPOINT
}

class JSONDataset(torch.utils.data.Dataset):
    def __init__(self, data_path):
        super(JSONDataset, self).__init__()

        with open(data_path) as fd:
            self.data = [json.loads(line) for line in fd]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

def postprocess_data(decoded):
    return [x.replace('<n>', ' ') for x in decoded]

def main(model, model_name_or_path, data_path):
      if not (model or model_name_or_path):
          raise ValueError('Model is required')

      if model and model_name_or_path:
          raise ValueError('Specify model or model_name_or_path but not both')

      if model:
          model_name_or_path = MODEL_CHECKPOINTS[model]
          file_model_name = model
      else:
          model_name_or_path = model_name_or_path
          file_model_name = model_name_or_path.replace("/", "-")
      model = AutoModelForSeq2SeqLM.from_pretrained(model_name_or_path).to(DEVICE)
      tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)

      dataset = JSONDataset(data_path)

      dataloader = torch.utils.data.DataLoader(dataset, batch_size=BATCH_SIZE)

      file_dataset_name = os.path.splitext(os.path.basename(data_path))[0]
      filename = f'{file_model_name}.{file_dataset_name}.predictions'
      fd_out = open(filename, 'w')

      model.eval()
      with torch.no_grad():
          for raw_data in tqdm(dataloader):
              batch = tokenizer(raw_data["document"], return_tensors="pt", truncation=True, padding="longest").to(DEVICE)
              summaries = model.generate(input_ids=batch.input_ids, attention_mask=batch.attention_mask)
              decoded = tokenizer.batch_decode(summaries, skip_special_tokens=True, clean_up_tokenization_spaces=False)
              for example in postprocess_data(decoded):
                  fd_out.write(example + '\n')


main('bart-xsum','','sample.json')
main('pegasus-xsum','','sample.json')
