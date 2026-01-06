#include <regex>
#include <string>
using namespace std;
struct AccessLog {
    string ip;
    string datetime;
    string method;
    string url;
    int status;
    int bytes;
};

AccessLog parseLogLine(const string& line) {
    regex pattern(
        R"((\S+) - - \[(.*?)\] \"(\S+) (\S+) \S+\" (\d{3}) (\d+))"
    );

    smatch match;
    if (regex_search(line, match, pattern)) {
        return {
            match[1],                 // IP
            match[2],                 // Date & time
            match[3],                 // HTTP method
            match[4],                 // URL
            stoi(match[5]),      // Status code
            stoi(match[6])       // Bytes
        };
    }
    return {};
}
