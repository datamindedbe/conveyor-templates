resource "azuread_application" "azureapp" {
  display_name = var.project_name
}

resource "azuread_service_principal" "azureapp" {
  application_id               = azuread_application.azureapp.application_id
  app_role_assignment_required = false
}

resource "azurerm_storage_container" "container" {
  name                  = var.project_name
  storage_account_name  = var.storage_account_name
  container_access_type = "private"
}

resource "azurerm_role_assignment" "blob_storage_read_access" {
  scope                = "/subscriptions/${var.subscription}/resourceGroups/${var.resource_group_name}/providers/Microsoft.Storage/storageAccounts/${var.project_name}"
  role_definition_name = "Storage Blob Data Contributor"
  principal_id         = azuread_service_principal.azureapp.id
}

resource "azuread_application_federated_identity_credential" "azureapp" {
  for_each = toset(var.namespaces)
  application_object_id = azuread_application.azureapp.object_id
  display_name          = "kubernetes-federated-identity-${var.project_name}-${each.key}"
  audiences             = ["api://AzureADTokenExchange"]
  issuer                = var.oidc_issuer_url
  subject               = "system:serviceaccount:${each.key}:${var.project_name}"
}