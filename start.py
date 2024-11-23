from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import pathlib
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def start():
    logger.info("Initializing model...")
    try:
        model_dir = pathlib.Path().resolve() / "models"
        model_name = "Qwen/Qwen2.5-0.5B-Instruct"
        
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype="auto",
            device_map="auto",
            cache_dir=model_dir
        )

        if torch.cuda.is_available():
            model.to("cuda")
            logger.info("Model moved to CUDA device.")
        else:
            logger.info("CUDA is not available.")
        
        logger.info(f"Model device: {model.device}")

    except Exception as e:
        logger.error(f"Error loading model: {str(e)}")
        raise e

if __name__ == "__main__":
    start()