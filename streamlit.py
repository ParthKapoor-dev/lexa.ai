import streamlit as st
from tokenizers import Tokenizer
import torch
from model import Seq2SeqTransformer, config

# Load tokenizer and model
tokenizer = Tokenizer.from_file('./model/tokenizer.json')
model = Seq2SeqTransformer(config)
state_dict = torch.load('./model/best_model.pt', map_location='cpu')
model.load_state_dict(state_dict)

# Special token map
special_tokens = {
    '<unk>': 0,
    '<pad>': 1,
    '<s-en>': 2,
    '<s-hi>': 3,
    '<s-te>': 4,
    '</s>': 5,
}

# Translation function
def translate(input_sentence, language='hi', deterministic=True, temperature=1.0):
    input_ids = f"<s-en>{input_sentence.strip()}</s>"
    input_ids = tokenizer.encode(input_ids).ids
    input_ids = torch.tensor(input_ids, dtype=torch.long).unsqueeze(0)
    bos = special_tokens[f"<s-{language}>"]
    outputs = model.generate(input_ids, deterministic=deterministic, bos=bos, temperature=temperature)
    translation = tokenizer.decode(outputs.numpy())
    return translation

# Streamlit UI
st.title("Lexa AI: Multilingual Translation App (English → Hindi/Telugu)")

input_text = st.text_area("Enter English text to translate", "")
language = st.selectbox("Select target language", options=["Hindi", "Telugu"])
sampling = st.checkbox("Use sampling (more creative)", value=True)
temperature = st.slider("Temperature (sampling randomness)", min_value=0.1, max_value=2.0, value=1.0, step=0.1)

if st.button("Translate"):
    if input_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        lang_code = "hi" if language == "Hindi" else "te"
        translation = translate(input_text, language=lang_code, deterministic=not sampling, temperature=temperature)
        st.success("Translation:")
        st.write(translation)
