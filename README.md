# Real-time Data Analysis with AWS Kinesis


In this hands-on project, we will work with a combination of AWS services to demonstrate real-time data ingestion, analysis, and processing. Specifically, we will be using:

- **Kinesis Data Streams**: To ingest and manage the streaming data.
- **Kinesis Data Analytics**: To perform real-time analytics on the streaming data.
- **Lambda**: To process the data and trigger specific actions.
- **DynamoDB**: To store and query the results of our analysis.

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
