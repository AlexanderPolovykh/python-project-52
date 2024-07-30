-- initialize postgres data base for Task Manager

DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name varchar(100) UNIQUE,
    full_name varchar(255),
    created_at date
);


-- CREATE TABLE url_checks (
--     id integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
--     url_id integer REFERENCES urls (id),
--     status_code smallint,
--     h1 varchar(255),
--     title varchar(255),
--     description varchar(255),
--     created_at date
-- );

INSERT INTO users (name, full_name, created_at) 
VALUES 
    ('alex', 'test test', '2024-07-29 12:01'), 
    ('swen', 'test2 test2', '2024-07-28 13:55');
