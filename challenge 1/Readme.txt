For setting up the 3 tier environment in Azure, Terraform is used.

Terraform Modules approach will be used to deploy all the required resources and it will help in re-usability of IaC code. The modules used will be
- compute (for VMs)
- database (for DB)
- newtworking (for Vnet and Subnets)
- resourcegroup (for RG)
- securitygroup (for NSGs)


Commom 3 tier environment consists of
- 1 resource group in which all required resources will be created
- 1 Vnet and 3 Subnets (Each VM with separate subnet)
- 3 VMs (for Web, App and DB and connectivity between them via NSG)
- Web VM will interact with internet, App VM will interect with Web VM and reply back to it and DB VM will connect to App VM
- 1 DB (Azure SQL DB)


Deployment steps
- terraform init (initialize the terraform modules and backend (we can use the local/remote backend))
- terraform validate (will validate the terraform scripts)
- terraform plan (will show what resources will be created)
- terraform apply -auto-approve (will deploy the resources)
