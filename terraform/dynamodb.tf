resource "aws_dynamodb_table" "products" {
  name         = var.dynamodb_table
  billing_mode = "PAY_PER_REQUEST"

  hash_key = "product_id"

  attribute {
    name = "product_id"
    type = "S"
  }

  point_in_time_recovery {
    enabled = true
  }

  server_side_encryption {
    enabled = true
  }

  tags = local.common_tags
}