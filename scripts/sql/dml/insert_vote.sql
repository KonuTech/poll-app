-- noinspection SpellCheckingInspectionForFile

-- noinspection SqlNoDataSourceInspectionForFile

INSERT INTO poll.votes (
     username
    ,option_id
) VALUES (%s, %s);
