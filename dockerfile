FROM python:3.9.13-slim-buster

WORKDIR C:/Users/saina/Desktop/DS_ML_AI/Scaler/Module_17_MLOPS/MLOPS_GIT/MLOPS_PRACTICE/

COPY requirements.txt ./

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python","-m","flask","--app","predictions.py","run","--host=0.0.0.0"]