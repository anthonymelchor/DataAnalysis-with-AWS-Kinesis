# Real-time Data Analysis with AWS Kinesis


In this hands-on project, we will work with a combination of AWS services to demonstrate real-time data ingestion, analysis, and processing. Specifically, we will be using:

- **Kinesis Data Streams**: To ingest and manage the streaming data.
- **Kinesis Data Analytics**: To perform real-time analytics on the streaming data.
- **Lambda**: To process the data and trigger specific actions.
- **DynamoDB**: To store and query the results of our analysis.

### Creating Cloud9 Enviroment
Initially, we will use the AWS Cloud9 service to execute our CloudFormation template.

1. Navigate to the Cloud9 service in the AWS console and create a new Cloud9 Environment.

![1](https://github.com/anthonymelchor/CICD-lambda-serverless/assets/48603061/efb98289-6337-4084-b620-b0a87d41674f)

2. Give it a name, and then leave all the defaults as in. Press the "Create" button to create the environment.

![2](https://github.com/anthonymelchor/CICD-lambda-serverless/assets/48603061/68e42bd1-0245-4b81-aa01-80b710b1617c)

## Creating Stacks
1. After the environment has been successfully created, open it up, and from the console, clone the current repository:
```
https://github.com/anthonymelchor/DataAnalysis-with-AWS-Kinesis.git
```
![3](https://github.com/anthonymelchor/CICD-lambda-serverless/assets/48603061/8dca9429-5caa-4ef1-a4f2-6bbd2616c7b0)

2.  Navigate to the 'CICD-lambda-serverless' project and then to the 'code_pipeline' folder. Execute the following command to create our first services stack:
```
sh codepipeline.sh
```
![4](https://github.com/anthonymelchor/CICD-lambda-serverless/assets/48603061/5bd9ef76-2711-4bf2-ad23-604b966fc234)

3. To validate that the process of creating the stack was successful, we can go into the AWS CloudFormation service, where we will visualize the 'codepipeline-transactions' stack and its resources:

![5](https://github.com/anthonymelchor/CICD-lambda-serverless/assets/48603061/8e2f282a-06fe-43c7-bebe-d9efaf21db69)

4. We will follow a similar process to create our second stack:

```
sh dynamodb.sh
```
![6](https://github.com/anthonymelchor/CICD-lambda-serverless/assets/48603061/8a354367-c143-4bb8-a61b-9058c074436a)

**Setting Up the Environment**:
   - Access AWS Cloud9 and create a new folder.
   - Upload the Python script `WriteStreamTransactions.py`, the dataset `transactions.csv`, and the `LabKDA.yaml` file.
   - Deploy the CloudFormation stack using the AWS CLI:
     ```
     aws cloudformation create-stack --stack-name StackLabKDA --template-body file://LabKDA.yaml --capabilities CAPABILITY_NAMED_IAM
     ```
   This will create the necessary resources, including a DynamoDB table, Kinesis Data Streams, a Lambda function, and a Kinesis Data Analytics application.

2. **Running the Lab**:
   - Open the Kinesis Data Analytics service and start the application by clicking on "Run."
   - Execute the Python script from Cloud9 to send 5000 transactions to Kinesis Data Streams:
     ```
     python3 WriteStreamTransactions.py
     ```

3. **Verification**:
   - Check the DynamoDB table to verify that it contains 7 records, which correspond to fraudulent transactions.

4. **Cleanup**:
   - Once you've finished the lab, remember to delete the CloudFormation stack to avoid unnecessary charges:
     ```
     aws cloudformation delete-stack --stack-name StackLabKDA
     ```

Feel free to reach out if you have any questions or encounter any issues. Happy learning!
