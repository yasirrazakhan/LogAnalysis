create view PopularArticles  as SELECT title, views
    FROM articles INNER JOIN (SELECT path, count(path) AS views
                       FROM log  GROUP BY log.path) AS log
					    ON log.path = '/article/' || articles.slug
					    ORDER BY views DESC LIMIT 3;

create view PopularAuthors as select name, count(title) as num
		from authors join articles on authors.id = articles.author join log on log.path = concat('/article/' , articles.slug)
		  group by name  order by num desc;

create view errorsrate as select date(time) as day,
		count(status) as erros from log where status != '200 OK' group by date(time);

create view totalrequests as select date(time) as day,
		count(status) as requests from log group by date(time);

create view errorsandrequests as select errorsrate.erros, totalrequests.requests
		 from errorsrate join totalrequests on errorsrate.day = totalrequests.day;

create view calpercentage as select erros, requests, (cast((erros) as float)/ cast((requests) as float)*100)
		as percentage from errorsandrequests;

create view q3query as select errorsrate.day, round(cast(calpercentage.percentage as numeric), 2) as percentage
	     from errorsrate join calpercentage on errorsrate.erros = calpercentage.erros where percentage > 1;