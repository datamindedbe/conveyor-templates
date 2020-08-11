variable "aws_account_id" {
  description = "The aws account id we are deploying to"
}
variable "aws_region" {
  description = "The aws region we are deploying to"
}
variable "env_name" {
  description = "The name of the datafy environment this is deployed to"
}
variable "env_worker_role" {
  description = "The name of the IAM role the kubernetes workers of datafy are using. This is needed for spark IAM roles"
}
variable "aws_iam_openid_connect_provider_url" {
  description = "The url of the open id connect provider of the EKS cluster. This is used when linking kubernetes service account to iam roles"
}
variable "aws_iam_openid_connect_provider_arn" {
  description = "The arn of the open id connect provider of the EKS cluster. This is used when linking kubernetes service account to iam roles"
}
