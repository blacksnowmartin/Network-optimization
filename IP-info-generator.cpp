#include <iostream>
#include <string>
#include <vector>
#include <bitset>

// Function to determine the class of an IPv4 address
std::string getIPAddressClass(const std::string& ipAddress) {
    unsigned int firstOctet = std::stoi(ipAddress.substr(0, ipAddress.find('.'));

    if (firstOctet >= 1 && firstOctet <= 126)
        return "Class A";
    else if (firstOctet >= 128 && firstOctet <= 191)
        return "Class B";
    else if (firstOctet >= 192 && firstOctet <= 223)
        return "Class C";
    else if (firstOctet >= 224 && firstOctet <= 239)
        return "Class D (Multicast)";
    else if (firstOctet >= 240 && firstOctet <= 255)
        return "Class E (Reserved)";
    else
        return "Invalid";
}

// Function to determine if the given IPv4 address is a broadcast address
bool isBroadcastAddress(const std::string& ipAddress) {
    return ipAddress == "255.255.255.255";
}

// Function to determine if the given IPv4 address is a unicast address
bool isUnicastAddress(const std::string& ipAddress) {
    return ipAddress != "0.0.0.0" && ipAddress != "255.255.255.255";
}

int main() {
    std::string ipAddress;

    // Input IPv4 address
    std::cout << "Enter an IPv4 address (e.g., 192.168.1.1): ";
    std::cin >> ipAddress;

    // Check if the input is a valid IPv4 address
    std::vector<int> octets;
    size_t startPos = 0;
    for (size_t i = 0; i < 4; i++) {
        size_t endPos = ipAddress.find('.', startPos);
        if (endPos == std::string::npos) {
            endPos = ipAddress.length();
        }

        std::string octetStr = ipAddress.substr(startPos, endPos - startPos);
        int octet = std::stoi(octetStr);

        if (octet < 0 || octet > 255) {
            std::cerr << "Invalid IPv4 address." << std::endl;
            return 1;
        }

        octets.push_back(octet);
        startPos = endPos + 1;
    }

    // Check if it's a valid IPv4 address
    if (octets.size() != 4) {
        std::cerr << "Invalid IPv4 address." << std::endl;
        return 1;
    }

    // Determine and display the details of the IPv4 address
    std::cout << "IP Address: " << ipAddress << std::endl;
    std::cout << "Class: " << getIPAddressClass(ipAddress) << std::endl;
    std::cout << "Is Unicast: " << (isUnicastAddress(ipAddress) ? "Yes" : "No") << std::endl;
    std::cout << "Is Broadcast: " << (isBroadcastAddress(ipAddress) ? "Yes" : "No") << std::endl;
    std::cout << "Binary Representation: ";
    for (int octet : octets) {
        std::cout << std::bitset<8>(octet) << ".";
    }
    std::cout << std::endl;

    return 0;
}
