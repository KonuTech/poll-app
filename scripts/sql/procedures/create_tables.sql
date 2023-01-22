-- PROCEDURE: poll.create_tables()

-- DROP PROCEDURE IF EXISTS poll.create_tables();

CREATE OR REPLACE PROCEDURE poll.create_tables(
	)
LANGUAGE 'plpgsql'
AS $BODY$
    BEGIN

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
      
    END;
    
$BODY$;

ALTER PROCEDURE poll.create_tables()
    OWNER TO iuqmdfly;
