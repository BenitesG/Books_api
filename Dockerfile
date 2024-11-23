# MySQL image
FROM mysql:8

# Adding SQL scripts to be executed when creating the database.
COPY ./db/ /docker-entrypoint-initdb.d/
