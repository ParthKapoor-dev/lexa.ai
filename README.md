# LEXA.AI: Multilingual Machine Translation with Transformers

> This project was for learning purposes only (submission for NLP subject). Hence, focused on getting decent results rather than building an alternative to existing multilingual models.

- Implemented a [7M parameter model](./model.py).
- Trained a BERT style tokenizer.
- Trained on [Opus100](https://huggingface.co/datasets/opus100) Dataset with `en-hi` & `en-te` subsets.
- Streamlit Frontend interface for basic testing

```
ENGLISH   --> HINDI
          |
          --> TELUGU
```

## Working

- The model understands which language to translate to based on the preceding beginning-of-sentence `bos` token:
  - english sentences start with `<s-en>` token
  - hindi sentences start with `<s-hi>` token
  - telugu sentences start with `<s-te>` token
  - all sentences end with `</s>` token
- trained as a Sequence-to-Sequence transformer model with an encoder-decoder style architecture. Encoder handles english and decoder handles both hindi & telugu.


## Model Config
```py
config = {
    'dim': 128,
    'n_heads': 4,
    'attn_dropout': 0.1,
    'mlp_dropout': 0.1,
    'depth': 8,
    'vocab_size': 30000,
    'max_len': 128
 }
```

## Dockerfile

```
# build
docker build -t lexa .

# run
docker run -p 8501:8501 -d lexa
```
