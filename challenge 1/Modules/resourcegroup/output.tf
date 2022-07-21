output "resource_group_name" {
    value = azurerm_resource_group.three-tier-env.name
    description = "Name of the resource group."
}

output "location_id" {
    value = azurerm_resource_group.three-tier-env.location
    description = "Location id of the resource group"
}
