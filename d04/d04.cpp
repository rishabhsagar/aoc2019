#include <iostream>
#include <vector>
#include <sstream>

// String manipulation and other int to str conversion

int ctoi(const char c) {
    return std::stoi(std::to_string(c));
}

std::vector<std::string> split(const std::string& s, char delimiter)
{
    std::vector<std::string> tokens;
    std::string token;
    std::istringstream ts(s);
    while (std::getline(ts, token, delimiter)) tokens.push_back(token);
    return tokens;
}


// Filter function

std::vector<std::string> find_password(int i_min, int i_max) {
    const auto is_valid = [i_min, i_max](int password) -> bool {
        int group = -1, prev = -1, remaining = -1;
        for (char c : std::to_string(password)) {
            int digit = ctoi(c);
            if (digit < prev) return false;
            if (digit == prev && digit != remaining && group == -1) group = digit;
            if (digit == prev && digit == remaining && group == digit) group = -1;
            remaining = prev;
            prev = digit;
        }
        return group != -1 && (password > i_min && password < i_max);
    };
    std::vector<std::string> valid_passwords{};

    for (int p = i_min; p < i_max; ++p) {
        if (is_valid(p)) {
            valid_passwords.push_back(std::to_string(p));
        }
    }

    return valid_passwords;
}

// Run conditional filters

int main() {
    const auto passwords = find_password(265275,781585);
    for (const std::string& pass : passwords) {
        std::cout << "Valid password: " << pass << std::endl;
    }

    std::cout << "Number of valid passwords: " << passwords.size() << std::endl;
    return 0;
}

// TIO
// https://tio.run/##jVRNb9swDL3rV7AdUFhosq4FshZxkuOOuwzYZRgCxZYTobZkSHI6rMhvz6gPO4qzDPPFMvn4SD6RLtp2ui2K4/GDkEXdlRwWQhmrOWtW5GTb88IqnVpMDyIPD/DNaiG30DAp2q5mVigJTJag7I5rENKCVYABUCi559qgnxBnRlaRodHgccfQT@GdAD6a205LjCnnc@NA/mTV2vhUWUFpTg6EeHOobhHBzr8C09bCRurEcQdmElKVvBaNsFxTElJepbLqlUuTn0DBEeyJWQR7EAasyQwN3redqDmEFrbc1kLyzGIdnmCSVEJjro9tZ3brDSteM2@IPFGUvh5s34n/RdQYC1UnC@uFvdpIJWS5bpkxb0qXmdNfrBuBFcQj@9XLH3RjHV6bMOs9q0UJS/jRwx30pyfo2ShMV7BRqo4E7nH@rVZdi6HTxwm0mu/jUfOGCelEdN/5EFIpDVmYBJjD6M6HXDRJ0icqxVZYZAsTRfNzQAVZACx8FbSXsmK14dewy2Uo@e4ust8sk8LRGptzLdChUw/9b8rlNUrvpol@55SpgI7x3BuVHpVyIKdo330gv3HsLvcgMKzCYDjjYFvECQl8h/zfO@NHZpg18454MlywHxyszyfJ8Ri5c7i/b9PLdcL185e1F/c@SpJszXhyKB3LcCDpSo2Y/G65Kp3I2V@WYkBiF@db9fR59vQ8mzy/PM5eZjFrmOrLX5ELwjEfyNL@PLBQHY7sAm6/@w3sgXO4dVYfjm8P5bKs87Szc4KvXbPBn4SqQqunnAlXENGI3xxbvuSNUn1CcY7HPw