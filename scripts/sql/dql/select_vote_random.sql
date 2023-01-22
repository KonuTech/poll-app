-- noinspection SpellCheckingInspectionForFile

-- noinspection SqlNoDataSourceInspectionForFile

SELECT
    *
FROM
    poll.votes
WHERE
    option_id = %s
ORDER BY
    RANDOM()
LIMIT 1;
