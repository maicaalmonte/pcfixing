# Type the following command to stop the indexing service:
net stop "Windows Search"
#To start the indexing service again, use:
net start "Windows Search"
# Rebuild the Index (via the search service):
 control /name Microsoft.IndexingOptions
# Run the following command to list all services and filter for "Search":
Get-Service | Where-Object { $_.DisplayName -like "*Search*"
# Check status
Get-Service -Name WSearch
# Open Indexing Options using the command you already used:
control /name Microsoft.IndexingOptions
# Check for Dependency Issues
Get-Service WSearch | Select-Object -ExpandProperty DependentServices
# Start any dependencies:
Start-Service -Name <dependent_service_name>
