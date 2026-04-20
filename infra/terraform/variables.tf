variable "ssh_fingerprint" {
  type        = string
  description = "SSH Key fingerprint for droplet access"
}

variable "do_token" {
  type        = string
  sensitive   = True
}
