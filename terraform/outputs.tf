output "bucket_name" {

  value = aws_s3_bucket.raw_bucket.bucket

}

output "dynamodb_table" {

  value = aws_dynamodb_table.products.name

}

output "lambda_role_arn" {

  value = aws_iam_role.lambda_role.arn

}

output "lambda_name" {

  value = aws_lambda_function.retail_pipeline.function_name

}

output "lambda_arn" {

  value = aws_lambda_function.retail_pipeline.arn

}