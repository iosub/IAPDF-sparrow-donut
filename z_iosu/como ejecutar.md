(sparrow-data) PS C:\IA\test\sparrow-donut\sparrow-data\api> python -m uvicorn endpoints:app --host 0.0.0.0 --port 8000

(sparrow-ml) PS C:\IA\test\sparrow-donut\sparrow-ml\api> python -m uvicorn endpoints:app --host 0.0.0.0 --port 8001

(sparrow-ui) PS C:\IA\test\sparrow-donut\sparrow-ui> .\.venv\Scripts\activate; streamlit run main.py --server.port 7860

crear los entornos virtuales
=================

(sparrow-data) PS C:\IA\test\sparrow-donut\sparrow-data\api> uv venv --python 3.10
(sparrow-ml) PS C:\IA\test\sparrow-donut\sparrow-ml\api> uv venv --python 3.10
(sparrow-ui) PS C:\IA\test\sparrow-donut\sparrow-ui> uv venv --python 3.10

=================
instalr dependencias

(sparrow-data) PS C:\IA\test\sparrow-donut\sparrow-data\api> pip install -r requirements.txt
(sparrow-ml) PS C:\IA\test\sparrow-donut\sparrow-ml\api> pip install -r requirements.txt
(sparrow-ui) PS C:\IA\test\sparrow-donut\sparrow-ui> pip install -r requirements.txt
