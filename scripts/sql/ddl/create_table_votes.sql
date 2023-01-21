-- noinspection SpellCheckingInspectionForFile

-- noinspection SqlNoDataSourceInspectionForFile

-- Table: poll.votes

-- DROP TABLE IF EXISTS poll.votes;

CREATE TABLE IF NOT EXISTS poll.votes
(
    username text COLLATE pg_catalog."default",
    option_id integer,
    CONSTRAINT votes_option_id_fkey FOREIGN KEY (option_id)
        REFERENCES poll.options (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS poll.votes
    OWNER to iuqmdfly;
