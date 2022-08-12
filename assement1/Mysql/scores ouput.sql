SELECT dense_rank() over(ORDER BY Score desc) as id_rank,
Score
 FROM marks.scores
 