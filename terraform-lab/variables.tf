variable "region" {
  description = "AWS region for the lab"
  type        = string
  default     = "us-east-1"
}

variable "vpc_cidr" {
  description = "CIDR block for the lab VPC and subnet"
  type        = string
  default     = "10.0.1.0/24"
}

variable "name_prefix" {
  description = "Prefix for all resource names"
  type        = string
  default     = "AutomationLab"
}
