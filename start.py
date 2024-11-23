from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import pathlib

from src.infra.services.logger_service import LoggerService

def start():
    logger = LoggerService()

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
        
        logger.info(f"Model device: {model.device}")

    except Exception as e:
        logger.error(f"Error loading model: {str(e)}")
        raise e

if __name__ == "__main__":
    start()