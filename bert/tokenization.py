# pip install transformers

from transformers import BertTokenizer

tz = BertTokenizer.from_pretrained("bert-base-cased")
print(tz.convert_tokens_to_ids(["characteristically"]))
sent = "He remains characteristically confident and optimistic."
print(tz.tokenize(sent))
print(tz.convert_tokens_to_ids(tz.tokenize(sent)))
