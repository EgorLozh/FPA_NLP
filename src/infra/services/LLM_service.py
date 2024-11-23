import pathlib
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

from logger_service import LoggerService


class LLMService:
    def __init__(self, model_name="Qwen/Qwen2.5-0.5B-Instruct"):
        model_dir = pathlib.Path().resolve().parent().parent()/"models"
        self.logger = LoggerService()

        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype="auto",
            device_map="auto",
            cache_dir=model_dir
        )
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=model_dir)

        if torch.cuda.is_available():
            self.cuda_available = True
            self.model.to("cuda")
    

    def generate(self, prompt, max_new_tokens=512):
        self.logger(f"Generating response for prompt: {prompt[:min(len(prompt), 50)]}...")

        messages = [
            {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
        text = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)
        generated_ids = self.model.generate(
            **model_inputs,
            max_new_tokens= max_new_tokens
        )
        generated_text = self.tokenizer.batch_decode(generated_ids)[0]

        self.logger(f"Generated response: {generated_text[:min(len(generated_text), 50)]}...")

        return generated_text

