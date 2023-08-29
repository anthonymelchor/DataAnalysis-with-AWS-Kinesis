# Real-time Data Analysis with AWS Kinesis

In this project, we will take a journey into the world of real-time data analysis using AWS Kinesis services. Our exploration will focus on the simulation of real-time detection for attempted fraudulent banking transactions.

As we go deeper, you'll learn more about how different parts of AWS work together nicely. Get ready to dive into the details of adding data, quickly understanding data as it comes in, and making data change in special ways.

- **Kinesis Data Streams:** Watch how data comes in and is looked after for streaming data.
- **Kinesis Data Analytics:** Immerse yourself in real-time analytics that provide instant insights as data streams in.
- **Lambda:** Experience the dynamism of data processing and triggered actions through Lambda functions.
- **DynamoDB:** Extend the value of your analysis by storing and querying results using DynamoDB.

### Creating Cloud9 Enviroment
Initially, we will use the AWS Cloud9 service to execute our CloudFormation template.

1. Navigate to the Cloud9 service in the AWS console and create a new Cloud9 Environment.

![1](https://github.com/anthonymelchor/CICD-lambda-serverless/assets/48603061/efb98289-6337-4084-b620-b0a87d41674f)

2. Give it a name, and then leave all the defaults as in. Press the "Create" button to create the environment.

![2](https://github.com/anthonymelchor/CICD-lambda-serverless/assets/48603061/68e42bd1-0245-4b81-aa01-80b710b1617c)

## Creating Stack
- After the environment has been successfully created, open it up, and from the console, clone the current repository:
```
https://github.com/anthonymelchor/DataAnalysis-with-AWS-Kinesis.git
```
![1](https://github.com/anthonymelchor/DataAnalysis-with-AWS-Kinesis/assets/48603061/42caebed-0687-4bb9-8629-7f038d8f888f)

- Navigate to the 'DataAnalysis-with-AWS-Kinesis' project. Execute the following command to create our services stack:
```
aws cloudformation create-stack --stack-name DataAnalysis --template-body file://template.yml --capabilities CAPABILITY_NAMED_IAM
```
This will create the necessary resources, including a DynamoDB table, Kinesis Data Streams, a Lambda function, and a Kinesis Data Analytics application.

![2](https://github.com/anthonymelchor/DataAnalysis-with-AWS-Kinesis/assets/48603061/1e297c5c-54d3-4d55-a810-a9099e119934)

To validate that the process of creating the stack was successful, we can go into the AWS CloudFormation service, where we will visualize the 'DataAnalysis' stack and its resources.

![3](https://github.com/anthonymelchor/DataAnalysis-with-AWS-Kinesis/assets/48603061/dfcc5d73-7e74-459c-b92f-cf21409f826e)

## Running the Data Analytics Applicaction
- Open the Amazon Kinesis service, go to 'Analytics applications,' and select the 'SQL applications' option.
- Click on the 'AnalyticsTransactions' application that was created and start it by clicking on "Run."

## Executing Python file

Now we will proceed to execute the Python file that was downloaded at the time of cloning the repository and that will serve as the data source for our data stream. But first, we will explain a bit about the process that will be performed during the execution. The WriteStreamTransactions.py Python file will read the 'transactions.csv' dataset, also downloaded from the repository, containing approximately 5000 transaction records, out of which 7 are classified as fraudulent transactions. These records will be sent to our Data Stream, where our Data Analytics application comes into play. This application will analyze the Data Stream records in real-time and apply a filter to identify fraudulent transactions. The destination of our Data Analytics application will be a lambda function, created in the stack, which will take the filtered records and add them to a DynamoDB table.
To execute the Python file, you should run the following code in cloud formation enviroment:

```
pip install boto3
pip install pandas
python3 WriteStreamTransactions.py
```
![4](https://github.com/anthonymelchor/DataAnalysis-with-AWS-Kinesis/assets/48603061/5f85f0ec-fffe-483c-b659-a0e681bae9ee)

## Validation
As we wrapped up the execution, we validated its success by checking the 'TransactionFraud' DynamoDB table. The presence of the expected 7 records, corresponding to fraudulent transactions, provided concrete validation of our real-time data analysis approach.

![5](https://github.com/anthonymelchor/DataAnalysis-with-AWS-Kinesis/assets/48603061/bb2fb9c4-dc7e-4690-a9a1-c16fa96865fd)

## Conclusion
In this hands-on project, we've delved into the exciting realm of real-time data analysis using AWS Kinesis services. Through this project, we've harnessed the power of various AWS components to showcase the end-to-end process of data ingestion, real-time analysis, and meaningful data processing.
Through this project, we've not only demonstrated the capabilities of AWS services but also showcased the practical application of these tools in real-world scenarios. I hope this hands-on experience has enriched your understanding of real-time data analysis with AWS Kinesis and inspired you to explore further.
Thank you for embarking on this journey of exploration and learning. 
Catch you on the flip side!



