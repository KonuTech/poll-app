-- noinspection SpellCheckingInspectionForFile

-- noinspection SqlNoDataSourceInspectionForFile

SELECT
    *
FROM poll.options
WHERE
    poll_id=%s
;
