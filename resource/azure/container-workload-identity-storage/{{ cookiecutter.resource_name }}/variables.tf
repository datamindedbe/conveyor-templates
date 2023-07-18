variable "resource_group_name" {
  description = "The resource group name in which to create resources"
}

variable "resource_group_location" {
  description = "The location of the resource group, f.e. westeurope"
}

variable "storage_account_name" {
  description = "The storage account name which you want to access from the container"
}

variable "subscription" {
  description = "The subscription in which you want to create resources"
}

variable "oidc_issuer_url" {
  description = "The oidc issuer of the kubernetes cluster"
}

variable "project_name" {
}

variable "namespaces" {
  description = "The kubernetes namespaces/environments in which you want to run your job"
  type        = list(string)
}