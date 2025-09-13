try:
    from pydantic.v1 import BaseSettings
except ImportError:
    from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    huggingface_key: str = ""
    sparrow_key: str = "demo_key"
    secure_key: str = "demo_secure"
    dataset_name: str = "katanaml-org/invoices-donut-data-v1"
    ocr_stats_file: str = "data/ocr_stats.json"
    
    class Config:
        env_file = ".env"


settings = Settings()
