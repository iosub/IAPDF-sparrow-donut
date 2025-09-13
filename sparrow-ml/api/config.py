try:
    from pydantic.v1 import BaseSettings
except ImportError:
    from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    huggingface_key: str = ""
    sparrow_key: str = "demo_key"
    secure_key: str = "demo_secure"
    model_name: str = "naver-clova-ix/donut-base-finetuned-cord-v2"
    donut_inference_stats_file: str = "data/donut_inference_stats.json"
    donut_training_stats_file: str = "data/donut_training_stats.json"
    donut_evaluate_stats_file: str = "data/donut_evaluate_stats.json"
    
    # Additional required settings for training and evaluation
    dataset: str = "katanaml-org/invoices-donut-data-v1"
    base_config: str = "naver-clova-ix/donut-base"
    base_processor: str = "naver-clova-ix/donut-base"
    base_model: str = "naver-clova-ix/donut-base"
    model: str = "naver-clova-ix/donut-base-finetuned-cord-v2"
    processor: str = "naver-clova-ix/donut-base-finetuned-cord-v2"
    inference_stats_file: str = "data/donut_inference_stats.json"
    training_stats_file: str = "data/donut_training_stats.json"
    evaluate_stats_file: str = "data/donut_evaluate_stats.json"
    
    class Config:
        env_file = ".env"


settings = Settings()