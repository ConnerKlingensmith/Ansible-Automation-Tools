output "vpc_id" {
  description = "The ID of the VPC"
  value = aws_vpc.lab.id
}

output "subnet_id" {
  description = "The ID of the subnet"
  value = aws_subnet.lab.id
}

output "security_group_id" {
  description = "The ID of the security group"
  value = aws_security_group.lab.id
}
