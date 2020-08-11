resource "aws_iam_role" "{{ cookiecutter.resource_name }}" {
  name               = "{{ cookiecutter.resource_name|replace('_', '-') }}-${var.env_name}"
  path               = "/datafy-dp-${var.env_name}/"
  assume_role_policy = data.aws_iam_policy_document.{{ cookiecutter.resource_name }}_assume_role.json
}

data "aws_iam_policy_document" "{{ cookiecutter.resource_name }}_assume_role" {
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