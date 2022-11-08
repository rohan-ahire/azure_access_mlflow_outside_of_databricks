# azure_access_mlflow_outside_of_databricks
Code to show how we can access mlflow or other databricks api from outside of databricks workspace. This is specific to Azure.

* This process assumes a Service Principal (SP) exists.
* There is a one-time step "one_time_steps.sh" required to assign the SP to the databricks workspace. This script needs the databricks token to be exported in the env. This token is the one that might be owned by the owner of the SP.
* Each script required certain variables to be exported in the environment before any of the scripts can be executed.
    * DATABRICKS_HOST
    * SP_CLIENT_ID
    * SP_CLIENT_SECRET
    * TENANT_ID


There are two ways to connect to databricks using the Azure SP.
* Using Azure Active Directory token - https://github.com/rohan-ahire/azure_access_mlflow_outside_of_databricks/blob/8a4080b5c134ecd8dd1abe32e2c4a3d163809ca2/mlflow_example_using_sp_aad_token.py#L42 
* Using Databricks PAT generated on behalf of the SP - https://github.com/rohan-ahire/azure_access_mlflow_outside_of_databricks/blob/8a4080b5c134ecd8dd1abe32e2c4a3d163809ca2/mlflow_example_using_sp_pat_token.py#L43
