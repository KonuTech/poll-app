SELECT
    *
FROM poll.votes
WHERE
    option_id = %s
;