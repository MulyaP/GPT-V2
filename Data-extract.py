import datasets
from tqdm import tqdm
# from transformers import GPT2Tokenizer

# Load the dataset
dataset = datasets.load_dataset('openwebtext/openwebtext.py', split='train')

# Print some examples
# for example in dataset.take(5):
#     print(example)


def write_dataset_to_file(file_path, length):
    with open(file_path, 'w', encoding='utf-8') as file:
        for i in tqdm(range(0, length), desc="Processing Batches"):
            text = dataset[i]['text']
            file.write(text+'<|endoftext|>')

train_file_path = 'train.txt'
val_file_path = 'val.txt'

write_dataset_to_file(train_file_path, 3013769)
write_dataset_to_file(val_file_path, 334864)
