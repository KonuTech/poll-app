-- PROCEDURE: poll.drop_tables()

-- DROP PROCEDURE IF EXISTS poll.drop_tables();

CREATE OR REPLACE PROCEDURE poll.drop_tables(
	)
LANGUAGE 'plpgsql'
AS $BODY$
    BEGIN

        DROP TABLE IF EXISTS poll.polls CASCADE;
        DROP TABLE IF EXISTS poll.options CASCADE;
        DROP TABLE IF EXISTS poll.votes CASCADE;

    END;

$BODY$;

ALTER PROCEDURE poll.drop_tables()
    OWNER TO iuqmdfly;
