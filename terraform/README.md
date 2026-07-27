# Terraform

GCP infrastructure for the **BIlingual AI** project. Remote state is stored in a shared GCS backend (`dark-tfstates`) hosted in the `darktheme-ops` project.

## Prerequisites

- `terraform >= 1.6, < 2.0` and `gcloud` installed
- Application Default Credentials: `gcloud auth application-default login` — must be the account with access to both `darktheme-ops` (state) and `bilingual-ai` (resources)
- The `darktheme-ops` project and `gs://dark-tfstates` state bucket exist (already bootstrapped)
- The `bilingual-ai` project exists with billing linked and the following APIs enabled:

  ```bash
  gcloud services enable \
    iam.googleapis.com \
    iamcredentials.googleapis.com \
    run.googleapis.com \
    --project bilingual-ai
  ```

## Usage

Use the `/terraform` skill — it handles init, fmt, validate, plan, and apply
with confirmation gates:

```bash
/terraform
```

Or run manually:

```bash
# Only on first checkout or after changing the backend block
terraform init

# Standard change loop
terraform plan -out=tfplan.out
terraform apply tfplan.out
```

State locking happens automatically via GCS object generation numbers — concurrent `apply`s on the same prefix are blocked with a clear error.

## Adding more Terraform projects

Point a new project's `terraform.tf` at the same backend bucket with a
different prefix:

```hcl
backend "gcs" {
  bucket = "dark-tfstates"
  prefix = "<new-project-name>"
}
```

State for the two projects stays fully isolated.
