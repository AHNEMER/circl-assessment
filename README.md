CirclTask🚀

a simple project that uses serverless framework to execute AWS Lamada functions through API request, the allows you to add and retrieve clients' data from s3 bucket database 💾📊



Setup Instructions:
Follow these steps to set up the project locally:


1. Clone the repository:

git clone https://github.com/your-username/circltask.git
cd circltask


2. Install dependencies:
   
npm install


4. Configure AWS credentials
   
Make sure your AWS CLI is configured correctly with aws configure.


5. Deploy the service
   
serverless deploy






Example Usage:

Uploading Customer Data (POST):

curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com"}' https://your-api-id.execute-api.us-east-1.amazonaws.com/uploadCustomer


Retrieving Customer Data (GET):

curl https://your-api-id.execute-api.us-east-1.amazonaws.com/getCustomers
