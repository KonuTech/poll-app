-- noinspection SpellCheckingInspectionForFile

-- noinspection SqlNoDataSourceInspectionForFile

INSERT INTO poll.polls (
     title
    ,owner_username
) VALUES (%s, %s) RETURNING id;