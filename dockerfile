FROM python:3.9-slim
WORKDIR /studymanagement-image
COPY ./ /studymanagement-image/
CMD [ "python", "main.py" ]
#termianl
#docker image build -t studymanagement-app:1.0
#docker tag studymanagement-app muhammadumair132/studymanagement-app:1.0