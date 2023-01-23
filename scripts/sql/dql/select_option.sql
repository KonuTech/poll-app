-- noinspection SpellCheckingInspectionForFile

-- noinspection SqlNoDataSourceInspectionForFile

SELECT
    *
FROM poll.options
WHERE
    id = %s
;