from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import pathlib

from src.infra.services.logger_service import LoggerService
from src.infra.services.video_service import VideoService
from src.infra.services.speech2text_service import Speech2TextService
from src.infra.services.LLM_service import LLMService

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
    
    # video_service = VideoService()
    # video_service.download_video('https://drive.google.com/file/d/1FrI5WEzdrp-tZom3xWmJJ2SDdSMTZMt2/view?usp=sharing', 'video.mp4', True)
    # video_service.extarct_audio('video.mp4', 'audio.mp3')

    speech2text_service = Speech2TextService()

    text = speech2text_service.recognize('audio.mp3')

    llm_service = LLMService()
    response = llm_service.generate(text+"""\n это был текст диалога двух человек,
    продавец рассказал покупателю о том что он продает синих китов это так? отвечай только да или нет""")

    print(response)
    

if __name__ == "__main__":
    start()