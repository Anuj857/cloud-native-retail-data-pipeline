data "archive_file" "lambda_zip" {

  type = "zip"

  source_dir = "${path.module}/../src"

  output_path = "${path.module}/lambda.zip"

}

resource "aws_lambda_function" "retail_pipeline" {

  function_name = "RetailPipelineLambda"

  filename = data.archive_file.lambda_zip.output_path

  source_code_hash = data.archive_file.lambda_zip.output_base64sha256

  role = aws_iam_role.lambda_role.arn

  handler = "lambda_function.lambda_handler"

  runtime = "python3.12"

  timeout = 60

  memory_size = 512

  environment {

    variables = {

      BUCKET_NAME = aws_s3_bucket.raw_bucket.bucket

      TABLE_NAME = aws_dynamodb_table.products.name

    }

  }

  depends_on = [

    aws_iam_role_policy_attachment.attach_policy

  ]

  tags = local.common_tags

}