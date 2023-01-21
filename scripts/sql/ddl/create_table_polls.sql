-- Table: poll.polls

-- DROP TABLE IF EXISTS poll.polls;

CREATE TABLE IF NOT EXISTS poll.polls
(
--     id integer NOT NULL DEFAULT nextval('poll.polls_id_seq'::regclass),
    id SERIAL,
    title text COLLATE pg_catalog."default",
    owner_username text COLLATE pg_catalog."default",
    CONSTRAINT polls_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS poll.polls
    OWNER to iuqmdfly;