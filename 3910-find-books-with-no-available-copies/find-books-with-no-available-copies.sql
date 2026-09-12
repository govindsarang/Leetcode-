# Write your MySQL query statement below
select l.book_id,l.title,l.author,l.genre,l.publication_year,COUNT(b.book_id) AS current_borrowers
from library_books l 
join borrowing_records b 
on l.book_id=b.book_id AND b.return_date is Null
group by l.book_id , l.total_copies
having count(b.book_id)=l.total_copies
order by  current_borrowers DESC,l.title ASC

