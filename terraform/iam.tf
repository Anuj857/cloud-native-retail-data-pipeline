resource "aws_iam_role" "lambda_role" {

  name = "RetailLambdaRole"

  assume_role_policy = jsonencode({

    Version = "2012-10-17"

    Statement = [

      {

        Effect = "Allow"

        Principal = {

          Service = "lambda.amazonaws.com"

        }

        Action = "sts:AssumeRole"

      }

    ]

  })

  tags = local.common_tags

}


resource "aws_iam_policy" "lambda_policy" {

  name = "RetailLambdaPolicy"

  policy = jsonencode({

    Version = "2012-10-17"

    Statement = [

      {

        Effect = "Allow"

        Action = [

          "logs:*"

        ]

        Resource = "*"

      },

      {

        Effect = "Allow"

        Action = [

          "s3:GetObject",
          "s3:PutObject",
          "s3:ListBucket"

        ]

        Resource = [

          aws_s3_bucket.raw_bucket.arn,
          "${aws_s3_bucket.raw_bucket.arn}/*"

        ]

      },

      {

        Effect = "Allow"

        Action = [

          "dynamodb:GetItem",
          "dynamodb:PutItem",
          "dynamodb:UpdateItem",
          "dynamodb:Scan"

        ]

        Resource = aws_dynamodb_table.products.arn

      }

    ]

  })

}


resource "aws_iam_role_policy_attachment" "attach_policy" {

  role = aws_iam_role.lambda_role.name

  policy_arn = aws_iam_policy.lambda_policy.arn

}