output "bucket_name" {

  value = aws_s3_bucket.raw_bucket.bucket

}

output "dynamodb_table" {

  value = aws_dynamodb_table.products.name

}

output "lambda_role_arn" {

  value = aws_iam_role.lambda_role.arn

}