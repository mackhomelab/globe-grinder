output "bucket_name" {
  value = aws_s3_bucket.assets.bucket
}

output "bucket_arn" {
  value = aws_s3_bucket.assets.arn
}

output "cloudfront_url" {
  value = aws_cloudfront_distribution.assets.domain_name
}