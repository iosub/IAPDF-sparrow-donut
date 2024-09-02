from pydantic import BaseSettings


class Settings(BaseSettings):
    #AQUI EL KEY
    huggingface_key: str = "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"
    sparrow_key: str = "io"
    processor: str = "katanaml-org/invoices-donut-model-v1"
    model: str = "katanaml-org/invoices-donut-model-v1"
    dataset: str = "katanaml-org/invoices-donut-data-v1"
    base_config: str = "naver-clova-ix/donut-base"
    base_processor: str = "naver-clova-ix/donut-base"
    base_model: str = "naver-clova-ix/donut-base"
    inference_stats_file: str = "data/donut_inference_stats.json"
    training_stats_file: str = "data/donut_training_stats.json"
    evaluate_stats_file: str = "data/donut_evaluate_stats.json"


settings = Settings()