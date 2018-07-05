# Log Analysis of a Newspaper Site:
In this Project we are going to analyze a newspaper site database with million rows  of data.
## Prerequisite
 - Python IDLE
 - POSTGRESQL

## Descripton and Design
  - This project uses **Python-DB Api** funciton to connect to *PostgreSQL* database.
  - It uses separate method for each query.
  - To setup file for this this project download the data file [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
  - Run the following command `psql -d [db name] -f newsdata.sql` this will import data in the file.
  - To test run the queries import **create_views** file by typing the following command `psql -d [db name] -f create_views.sql`.
  - You are know setup to test the project.

### Acknowledgment
- A very big thank you to Udacity Full Stack Nano-degree
### Developer
- **[`Linkedin`](https://linkedin.com/in/yasirrazakhan/)**
- **[`Twitter`](https://twitter.com/yasirrazakhan93)**