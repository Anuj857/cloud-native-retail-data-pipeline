resource "aws_s3_bucket" "raw_bucket" {

  bucket = var.bucket_name

  tags = local.common_tags
}

resource "aws_s3_bucket_versioning" "versioning" {

  bucket = aws_s3_bucket.raw_bucket.id

  versioning_configuration {

    status = "Enabled"

  }

}

resource "aws_s3_bucket_server_side_encryption_configuration" "encryption" {

  bucket = aws_s3_bucket.raw_bucket.id

  rule {

    apply_server_side_encryption_by_default {

      sse_algorithm = "AES256"

    }

  }

}

resource "aws_s3_bucket_public_access_block" "public_access" {

  bucket = aws_s3_bucket.raw_bucket.id

  block_public_acls       = true
  ignore_public_acls      = true
  block_public_policy     = true
  restrict_public_buckets = true

}

resource "aws_s3_bucket_lifecycle_configuration" "lifecycle" {
  bucket = aws_s3_bucket.raw_bucket.id

  rule {
    id     = "archive-old-files"
    status = "Enabled"

    filter {
      prefix = ""
    }

    transition {
      days          = 30
      storage_class = "STANDARD_IA"
    }

    expiration {
      days = 365
    }
  }
}