-- noinspection SpellCheckingInspectionForFile

-- noinspection SqlNoDataSourceInspectionForFile

INSERT INTO poll.votes (
     username
    ,option_id
    ,vote_timestamp
) VALUES (%s, %s, %s)
;
