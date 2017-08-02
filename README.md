# TermProject
## Analysis of jobs using Mongodb and Python
Retrieve jobs from multiple job api's and store them in MongoDB. Perform analysis of the jobs using MongoDB query language.

A quick glance of the project structure and a brief description of the files is given below:

### Project Structure

```{}
TermProject  
|_  
  Analysis  
  |_  
    Data  
    |_  
      Makefile.txt
      gather_data_dice.py
      gather_data_glassdoor.py
  |_
    analysis.py
|_
  Paper
    |_
      Report.html
      Report.pdf
      Report.Rmd
      Report.md
```

  * `Makefile.txt`            - Instructions for recreating the analysis.
  * `gather_data_dice.py`     - Downloads jobs from dice api and stores in mongodb.
  * `gather_data_glassdoor.py`- Downloads jobs from glassdoor api into mongodb.
  * `analysis.py`             - Contains functions used in the analysis.
  * `Report.pdf`              - A report of the analysis.
  * `Report.md`               - Markdown file that renders on Github as a webpage.

