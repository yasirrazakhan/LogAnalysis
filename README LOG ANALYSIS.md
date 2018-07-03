# Log Analysis of a Newspaper Site:
In this Project we are going to analyze a newspaper site database with million rows  of data. 
## Prerequisite
 - Python IDLE
 - POSTGRESQL
## Descripton and Design
  - This project uses **Python-DB Api** funciton to connect to *PostgreSQL* database.
  - It uses separate method for each question.
  - It also uses views to create customized table and analyze data more easily, Here is the description of each view used.
    1. `create view` ***PopularArticles**  as select title, count(path) as views from articles join log on  log.path = concat('/article/', articles.slug) group by title order by views desc limit 3*;
    2. `create view` ***PopularAuthors** as select name , count(title) as num from authors join articles on authors.id = articles.author join log on log.path = concat('/article/' , articles.slug) group by name  order by num desc;*
    3. `create view` ***errorsrate** as select date(time) as dasy, count(status) as erros from log where status != '200 OK' group by date(time);*
    4. `create view` ***totalrequests** as select date(time) as day, count(status) as request from log group by date(time);*
    5. `create view` ***errorsandrequests** as select errorsrate.erros, totalrequests.requests from errorsrate join totalrequests on errorsrate.day = totalrequests.day;*
    6. `create view` ***calpercentage** as select erros, requests, (cast((erros) as float)/ cast((requests) as float)*100) as percentage from errors and requests;*
    7. `create view` ***q3querry** as select errorsrate.day, round(cast(calpercentage.percentage as numeric), 2) as percentage from errorsrate join calpercentage on errorsrate.erros = calpecentage.erros where percentage > 1;*
### Acknowledgment
- A very big thank you to Udacity Full Stack Nano-degree
### Developer
- **[`Linkedin`](https://linkedin.com/in/yasirrazakhan/)**
- **[`Twitter`](https://twitter.com/yasirrazakhan93)**