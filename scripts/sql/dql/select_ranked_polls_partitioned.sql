-- noinspection SpellCheckingInspectionForFile

-- noinspection SqlNoDataSourceInspectionForFile

SELECT
     p.title
    ,o.option_text
    ,COUNT(v.username) AS vote_count
    ,RANK() OVER(PARTITION BY p.title ORDER BY COUNT(v.username)  DESC) AS rank
    ,DENSE_RANK() OVER(PARTITION BY title ORDER BY COUNT(v.username)  DESC) AS dense_rank
    ,ROW_NUMBER() OVER(PARTITION BY p.title ORDER BY COUNT(v.username)  DESC) AS row
FROM poll.polls AS p
LEFT JOIN poll.options AS o
ON p.id = o.poll_id
LEFT JOIN poll.votes AS v
ON o.id = v.option_id
GROUP BY
     p.title
    ,o.option_text
;