locals {
  project_name = "{{ cookiecutter.project_name }}"
  uuid_pattern = "????????-????-????-????-????????????"
}

resource "aws_iam_role" "{{ cookiecutter.resource_name }}" {
  name               = "{{ cookiecutter.resource_name|replace('_', '-') }}-${var.env_name}"
  assume_role_policy = data.aws_iam_policy_document.{{ cookiecutter.resource_name }}_assume_role.json
}

data "aws_iam_policy_document" "{{ cookiecutter.resource_name }}_assume_role" {
  statement {
    actions = ["sts:AssumeRoleWithWebIdentity"]
    effect  = "Allow"

    condition {
      test     = "StringLike"
      variable = "${replace(var.aws_iam_openid_connect_provider_url, "https://", "")}:sub"
      values   = ["system:serviceaccount:${var.env_name}:${replace(local.project_name, "_", ".")}-${local.uuid_pattern}"]
    }

    principals {
      identifiers = [var.aws_iam_openid_connect_provider_arn]
      type        = "Federated"
    }
  }
}

resource "aws_iam_role_policy" "{{ cookiecutter.resource_name }}" {
  name   = "{{ cookiecutter.resource_name|replace('_', '-') }}"
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

  statement {
    actions = [
      "glue:GetDatabase"
    ]
    resources = [
      "*"
    ]
    effect = "Allow"
  }

  statement {
    actions = [
      "glue:*"
    ]
    resources = [
      "arn:aws:glue:${var.aws_region}:${var.aws_account_id}:catalog",
      "arn:aws:glue:${var.aws_region}:${var.aws_account_id}:database/{{ cookiecutter.database_name }}",
      "arn:aws:glue:${var.aws_region}:${var.aws_account_id}:table/{{ cookiecutter.database_name }}/*"
    ]
    effect = "Allow"
  }
}
