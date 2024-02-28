FROM python:3
ADD rfc.py /
CMD [ "python", "./rfc.py" ]
