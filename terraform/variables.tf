variable "project_id" {
  description = "Google Cloud project ID"
  type        = string
  default     = "devops-project-460606"
}

variable "region" {
  description = "Google Cloud region"
  type        = string
  default     = "us-central1"
}

variable "cluster_name" {
  description = "Name of the GKE cluster"
  type        = string
  default     = "devops-cluster"
}
