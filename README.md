# Coingecko ETL Pipeline
![ETL Pipeline V3 (1)](https://user-images.githubusercontent.com/15370486/164557107-b26201bb-a6e5-45c4-853a-e01faa3d9c5d.png)


# Introduction & Goals
This project aims to extract data from Coingecko API into AWS RDS, then take recurring snapshots of RDS and export to S3, which will trigger a lambda function to call a glue workflow; the glue workflow will be responsible for transforming and loading into a final S3 sink. 

My goal was to create an ETL pipeline given the following usecase/scenario:

Hired by a small investment firm that wants to diversify their portfolio to digital assets. 
Their analytics team wants data about cryptocurrencies that they can query, create visualizations on, and etc. 
This department specifically wants a a dataset that include the following categories of cryptocurrencies:

- Smart Contract Platforms
- GameFi
- Meme Coins


# Contents
- [The Data Set](#the-data-set)
- [Used Tools](#used-tools)
  - [Connect](#connect)
  - [Buffer](#buffer)
  - [Processing](#processing)
  - [Storage](#storage)
  - [Visualization](#visualization)
- [Demo](#demo)
- [Conclusion](#conclusion)
- [Follow Me On](#follow-me-on)



# The Data Set
The data set I used was the Coingecko API. Coingecko is one of the most used oracle websites to track cryptocurrency prices. 

I chose this data source because:
1) Coingecko has great API documentation, 
2) free-tier usage for API get requests, 
3) and a massive amount of data on almost all cryptocurrencies. 

Nevertheless, some of the problems in this dataset include:
1) limited endpoints; not all historical data is available for all cryptocurrencies
2) low free tier rate limit on get requests; it is very easy to go over the requests limit for the API depending on what data you want to pull.

For my specific use case, I want to pull data from 3 different cryptocurrency categories:

- Smart Contract Platforms
- GameFi
- Meme Coins


# Used Tools

**Storage:**
------------
AWS RDS - AWS offers free tier for either MySQL or PostGres engine for RDS. I am more familiar with PostGres, but I chose RDS because all my backup, maintenance, and updates are handled by AWS.

AWS S3 - The simplest store for unstructured data for my purposes was S3. AWS offers great free tier benefits with S3, so it was the prime choice for a staging sink and final sink. 

**Orchestration:**
------------------
AWS Glue Workflows - I chose glue workflows to orchestrate any glue services because glue provides native graph interface via workflows to monitor and debug. 

AWS StepFunctions - In order to automate RDS Snapshot creation and exports, I chose to use StepFunctions because it provided the most visibility compared to event-driven monitoring such as CloudWatch/Eventbridge.

**ETL / Data Processing**
-------------------------
AWS Glue - Instead of using multiple lambdas, I ended up going with Glue because it is AWS's premier ETL tool. Though I would have a bit more configuration in terms of automation and integration with other services with lambdas / event driven framework, I chose to keep it simple because my use case is not complicated. Further, I have many "long-running-tasks" in my pipeline that would not be suited for Lambdas because of their 15 minute time limit.

## Connect

I connected to the Coingecko API using a manual python script. In the python script, I created different functions to defeat pagination, turn the requested data into 3 dataframes via pandas, and do an intial load into a postgres instance using SQL alchemy module. 

## Buffer

My chosen staging layer was an initial load to an RDS instance in AWS. This initial load is meant as a buffer before the processing / transformation happens via AWS Glue and then loaded to the final sink of an S3 bucket. The data inside this PostGres instance is structured because it was loaded via SQL alchemy, but not properly schematized yet. In short, the data is still raw, and in need of transformations. 

## Processing

I chose batch processing for this ETL pipeline. The processing tool I used was AWS Glue, and the transformations I applied to the data was mapping each column to the correct data types, and dropping an unnecessary column. 

## Storage

For my intermediary storage and final sink, I chose Amazon Simple Storage Service (S3). This object storage was easy for me to use, and I was able to use AWS Lambda as tool to automate tasks based that trigger if events happen in specific S3 buckets. 

## Visualization

I chose to not use a dedicated visualization tool for this project, but am aware I could have used AWS Quicksight or other tools to make a simple dashboard. Instead, I used S3 query select in order to confirm if my transformations indeed were applied to the data in the final sink. 


# Demo
- You could add a demo video here
- Or link to your presentation video of the project

# Conclusion
Write a comprehensive conclusion.
- How did this project turn out
- What major things have you learned
- What were the biggest challenges

# Follow Me On
LinkedIn - https://www.linkedin.com/in/patrick-de-paula/

# Appendix

[Markdown Cheat Sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
