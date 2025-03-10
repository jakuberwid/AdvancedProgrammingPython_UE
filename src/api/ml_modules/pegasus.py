from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch


# def pegasus_summarizer(text, max_length):
#     model_name = 'google/pegasus-xsum'
#     torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
#     tokenizer = PegasusTokenizer.from_pretrained(model_name)
#     model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)
#     batch = tokenizer.prepare_seq2seq_batch(text, truncation=True, padding='longest', return_tensors='pt',
#                                             max_length=max_length)
#     translated = model.generate(**batch)
#     tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
#     return tgt_text

class PegasusSummarizer:
    def __init__(self):
        self.model_name = 'google/pegasus-xsum'
        self.torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.tokenizer = PegasusTokenizer.from_pretrained(self.model_name)
        self.model = PegasusForConditionalGeneration.from_pretrained(self.model_name).to(self.torch_device)

    def summarize(self, text, max_length):
        batch = self.tokenizer(text, padding='longest', return_tensors='pt', max_length=max_length)
        translated = self.model.generate(**batch, max_new_tokens=max_length)
        tgt_text = self.tokenizer.batch_decode(translated, skip_special_tokens=True)
        return tgt_text


if __name__ == "__main__":
    text_example = open("example/text_example.txt", "r").read()
    # summary_text = pegasus_summarizer(text_example.txt, max_length=100)
    ps = PegasusSummarizer()
    summary_text = ps.summarize(text_example, max_length=60)
    print(summary_text)
