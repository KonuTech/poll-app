-- noinspection SpellCheckingInspectionForFile

-- noinspection SqlNoDataSourceInspectionForFile

SELECT
    *
FROM poll.polls AS p
INNER JOIN poll.options AS o
ON p.id=o.poll_id
WHERE
    p.id=%s
;
