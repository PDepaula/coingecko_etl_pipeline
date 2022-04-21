# Coingecko ETL Pipeline: My first semi-automated ETL pipeline

This project aims to extract data from Coingecko API into AWS RDS, then take recurring snapshots of RDS and export to S3, which will trigger a lambda function to call a glue workflow; the glue workflow will be responsible for transforming and loading into a final S3 sink. 



# Use Case / Scenario
Hired by a small investment firm that wants to diversify their portfolio to digital assets. 
Their analytics team wants data about cryptocurrencies that they can query, create visualizations on, and etc. 
This department specifically wants a a dataset that include the following categories of cryptocurrencies:

- Smart Contract Platforms
- GameFi
- Meme Coins


# Proposed Solution
![ETL Pipeline V3 (1)](https://user-images.githubusercontent.com/15370486/164557107-b26201bb-a6e5-45c4-853a-e01faa3d9c5d.png)


# Tool choice & Reasoning

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
