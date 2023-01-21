-- noinspection SpellCheckingInspectionForFile

-- noinspection SqlNoDataSourceInspectionForFile

SELECT
    *
FROM
    votes
WHERE
    option_id = %s
ORDER BY
    RANDOM()
LIMIT 1;
