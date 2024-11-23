USE DB_NAME;

-- Suggested name
CREATE TABLE books (
    id INTEGER NOT NULL auto_increment,
    title varchar(100),
    writer varchar(100),
    PRIMARY KEY (id)
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;

-- Suggested names
INSERT INTO books (title, writer) VALUES ("The Pragmatic Programmer: Your Journey to Mastery", "David Thomas");
INSERT INTO books (title, writer) VALUES ("Clean Code: A Handbook of Agile Software Craftsmanship", "Robert C. Martin");
INSERT INTO books (title, writer) VALUES ("Code Complete", "S. McConnell");