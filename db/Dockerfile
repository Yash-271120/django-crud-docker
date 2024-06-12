FROM mongo

COPY init.json /init.json

CMD mongoimport --uri mongodb://mongo:27017/test_db --collection todos --type json --file /init.json --jsonArray