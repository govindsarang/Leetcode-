
SELECT
    s.student_id,
    s.subject,
    f.score AS first_score,
    l.score AS latest_score
FROM Scores s
JOIN Scores f
    ON f.student_id = s.student_id
    AND f.subject = s.subject
    AND f.exam_date = (
        SELECT MIN(exam_date)
        FROM Scores
        WHERE student_id = s.student_id
          AND subject = s.subject
    )
JOIN Scores l
    ON l.student_id = s.student_id
    AND l.subject = s.subject
    AND l.exam_date = (
        SELECT MAX(exam_date)
        FROM Scores
        WHERE student_id = s.student_id
          AND subject = s.subject
    )
GROUP BY s.student_id, s.subject, f.score, l.score
HAVING COUNT(DISTINCT s.exam_date) >= 2
   AND l.score > f.score
ORDER BY s.student_id, s.subject;
