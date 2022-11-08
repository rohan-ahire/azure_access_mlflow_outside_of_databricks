# Script to assign SP to databricks workspace
# This is required as a one time step for each SP

# Export the host, token and Client ID in the environment
# export DATABRICKS_HOST=""
# export DATABRICKS_TOKEN=""
# export SP_CLIENT_ID=""


curl --location --request POST $DATABRICKS_HOST'/api/2.0/preview/scim/v2/ServicePrincipals' \
--header 'Authorization: Bearer '"$DATABRICKS_TOKEN" \
--header 'Content-Type: text/plain' \
--data-raw '{
  "applicationId": "'$SP_CLIENT_ID'",
  "displayName": "service_principal",
  "entitlements": [
    {
      "value": "allow-cluster-create"
    }
  ],
  "groups": [
    {
      "value": "admins"
    }
  ],
  "schemas": [ "urn:ietf:params:scim:schemas:core:2.0:ServicePrincipal" ],
  "active": true
}'
