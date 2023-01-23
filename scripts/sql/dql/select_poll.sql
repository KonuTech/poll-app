-- noinspection SpellCheckingInspectionForFile

-- noinspection SqlNoDataSourceInspectionForFile

SELECT
    *
FROM poll.polls
WHERE
    id = %s
;