-- noinspection SqlNoDataSourceInspectionForFile

-- Table: poll.options

-- DROP TABLE IF EXISTS poll.options;

CREATE TABLE IF NOT EXISTS poll.options
(
--     id integer NOT NULL DEFAULT nextval('poll.options_id_seq'::regclass),
    id SERIAL,
    option_text text COLLATE pg_catalog."default",
    poll_id integer,
    CONSTRAINT options_pkey PRIMARY KEY (id),
    CONSTRAINT options_poll_id_fkey FOREIGN KEY (poll_id)
        REFERENCES poll.polls (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS poll.options
    OWNER to iuqmdfly;
