from transformers import AutoModelForCausalLM, AutoTokenizer
import pathlib

def start():
    model_dir = pathlib.Path().resolve()/"models"
    model_name = "Qwen/Qwen2.5-0.5B-Instruct"

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype="auto",
        device_map="auto",
        cache_dir=model_dir
    )


if __name__ == "__main__":
    start()
    