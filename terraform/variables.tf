variable "aws_region" {
  description = "AWS Region"
  type        = string
}

variable "project_name" {
  description = "Project Name"
  type        = string
}

variable "environment" {
  description = "Environment"
  type        = string
}

variable "bucket_name" {
  description = "Unique S3 Bucket Name"
  type        = string
}

variable "dynamodb_table" {
  description = "DynamoDB Table Name"
  type        = string
}