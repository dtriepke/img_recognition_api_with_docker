FROM tensorflow/tensorflow
COPY ./main /user/local/python/
EXPOSE 5000
WORKDIR /user/local/python/
RUN pip install -r requirement.txt
CMD python flask_api_predict.py