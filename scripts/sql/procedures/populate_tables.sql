-- PROCEDURE: poll.populate_tables()

-- DROP PROCEDURE IF EXISTS poll.populate_tables();

CREATE OR REPLACE PROCEDURE poll.populate_tables(
	)
LANGUAGE 'plpgsql'
AS $BODY$
    BEGIN

        INSERT INTO poll.polls VALUES (1, 'Flask vs. Django', 'jose');
        INSERT INTO poll.polls VALUES (2, 'Python vs. Java', 'rolf');
        INSERT INTO poll.polls VALUES (3, 'Windows vs. Mac', 'bob');

        INSERT INTO poll.options VALUES (1, 'Flask', 1);
        INSERT INTO poll.options VALUES (2, 'Django', 1);
        INSERT INTO poll.options VALUES (3, 'It Depends', 1);
        INSERT INTO poll.options VALUES (4, 'Python', 2);
        INSERT INTO poll.options VALUES (5, 'Java', 2);
        INSERT INTO poll.options VALUES (6, 'Windows', 3);
        INSERT INTO poll.options VALUES (7, 'Mac', 3);

        INSERT INTO poll.votes VALUES ('jose', 1);
        INSERT INTO poll.votes VALUES ('charlie', 1);
        INSERT INTO poll.votes VALUES ('ammar', 1);
        INSERT INTO poll.votes VALUES ('rolf', 2);
        INSERT INTO poll.votes VALUES ('bob', 2);
        INSERT INTO poll.votes VALUES ('anne', 4);
        INSERT INTO poll.votes VALUES ('eric', 4);
        INSERT INTO poll.votes VALUES ('jose', 4);
        INSERT INTO poll.votes VALUES ('charlie', 4);
        INSERT INTO poll.votes VALUES ('ammar', 4);
        INSERT INTO poll.votes VALUES ('rolf', 4);
        INSERT INTO poll.votes VALUES ('bob', 4);
        INSERT INTO poll.votes VALUES ('anne', 5);
        INSERT INTO poll.votes VALUES ('eric', 5);
        INSERT INTO poll.votes VALUES ('bob', 4);
        INSERT INTO poll.votes VALUES ('anne', 6);
        INSERT INTO poll.votes VALUES ('eric', 7);

    END;
    
$BODY$;

ALTER PROCEDURE poll.populate_tables()
    OWNER TO iuqmdfly;
