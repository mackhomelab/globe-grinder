module "storage" {

  source = "./modules/storage"

  bucket_name = "globe-grinder-dev-04008"
  environment = "dev"
}
