#include <iostream>
#include <Windows.h>

int main() {
    SC_HANDLE scManager = OpenSCManager(NULL, NULL, SC_MANAGER_ALL_ACCESS);
    if (scManager == NULL) {
        std::cerr << "Failed to open service manager." << std::endl;
        return 1;
    }

    SC_HANDLE service = OpenService(scManager, "WSearch", SERVICE_START);
    if (service == NULL) {
        std::cerr << "Failed to open Windows Search service." << std::endl;
        return 1;
    }

    if (StartService(service, 0, NULL)) {
        std::cout << "Windows Search service started successfully." << std::endl;
    } else {
        std::cerr << "Failed to start Windows Search service." << std::endl;
    }

    CloseServiceHandle(service);
    CloseServiceHandle(scManager);
    return 0;
}
