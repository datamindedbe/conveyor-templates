locals {
  {{ cookiecutter.resource_name }}_service_account_name = "{{ cookiecutter.resource_name|replace('_', '-') }}-${var.env_name}"
}

resource "kubernetes_service_account" "{{ cookiecutter.resource_name }}" {
  metadata {
    name = local.{{ cookiecutter.resource_name }}_service_account_name
    namespace = var.env_name
    annotations = {
      "eks.amazonaws.com/role-arn" : aws_iam_role.{{ cookiecutter.resource_name }}.arn
    }
  }
  automount_service_account_token = true
}

resource "aws_iam_role" "{{ cookiecutter.resource_name }}" {
  name               = "{{ cookiecutter.resource_name|replace('_', '-') }}-${var.env_name}"
  path               = "/datafy-dp-${var.env_name}/"
  assume_role_policy = data.aws_iam_policy_document.{{ cookiecutter.resource_name }}_assume_role.json
}

data "aws_iam_policy_document" "{{ cookiecutter.resource_name }}_assume_role" {
  statement {
    actions = ["sts:AssumeRoleWithWebIdentity"]
    effect  = "Allow"

    condition {
      test     = "StringEquals"
      variable = "${replace(var.aws_iam_openid_connect_provider_url, "https://", "")}:sub"
      values   = ["system:serviceaccount:${var.env_name}:${local.{{ cookiecutter.resource_name }}_service_account_name}"]
    }

    principals {
      identifiers = [var.aws_iam_openid_connect_provider_arn]
      type        = "Federated"
    }
  }
}

resource "aws_iam_role_policy" "{{ cookiecutter.resource_name }}" {
  name   = "{{ cookiecutter.resource_name }}"
  role   = aws_iam_role.{{ cookiecutter.resource_name }}.id
  policy = data.aws_iam_policy_document.{{ cookiecutter.resource_name }}.json
}

data "aws_iam_policy_document" "{{ cookiecutter.resource_name }}" {
  statement {
    actions = [
      "s3:*"
    ]
    resources = [
      "arn:aws:s3:::{{ cookiecutter.bucket_name }}",
      "arn:aws:s3:::{{ cookiecutter.bucket_name }}/*"
    ]
    effect = "Allow"
  }
}
