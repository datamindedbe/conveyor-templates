locals {
  project_name = {{ cookiecutter.project_name }}
}

resource "aws_iam_role" "default" {
  name               = "${local.project_name}-${var.env_name}"
  assume_role_policy = data.aws_iam_policy_document.default_assume_role.json
}

data "aws_iam_policy_document" "default_assume_role" {
  statement {
    actions = [
      "sts:AssumeRole"
    ]
    principals {
      type        = "AWS"
      identifiers = [var.env_worker_role]
    }
    effect = "Allow"
  }
}

resource "aws_iam_role_policy" "default" {
  name   = "${local.project_name}-${var.env_name}"
  role   = aws_iam_role.default.id
  policy = data.aws_iam_policy_document.default.json
}

data "aws_iam_policy_document" "default" {
  statement {
    actions = [
      "s3:*"
    ]
    resources = [
      "arn:aws:s3:::*",
    ]
    effect = "Allow"
  }
}