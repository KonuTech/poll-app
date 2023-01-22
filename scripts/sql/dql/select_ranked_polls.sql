SELECT
     p.title
--     ,o.option_text
    ,COUNT(v.username) AS vote_count
    ,RANK() OVER(ORDER BY COUNT(v.username)) AS ranking
FROM poll.polls AS p
LEFT JOIN poll.options AS o
ON p.id = o.poll_id
LEFT JOIN poll.votes AS v
ON o.id = v.option_id
GROUP BY
     p.title
--     ,o.option_text
;
