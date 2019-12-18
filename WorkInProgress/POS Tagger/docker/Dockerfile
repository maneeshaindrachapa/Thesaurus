FROM python:3.6

WORKDIR /src/

COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080


# Download NLTK tokenization model
RUN python -m nltk.downloader -d /usr/local/share/nltk_data punkt
RUN pip install git+git://github.com/facebookresearch/fastText.git



