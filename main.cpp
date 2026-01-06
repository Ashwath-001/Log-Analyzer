#include <iostream>
#include <fstream>
#include <vector>
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

AccessLog parseLogLine(const string& line);
void analyzeLogs(const vector<AccessLog>& logs, const string& reportPath);

int main(int argc, char* argv[]) {
    if (argc < 3) {
        cout << "Usage: ./analyzer <access.log> <report.txt>\n";
        return 1;
    }

    ifstream file(argv[1]);
    if (!file.is_open()) {
        cout << "Error: Cannot open log file\n";
        return 1;
    }

    vector<AccessLog> logs;
    string line;

    while (getline(file, line)) {
        AccessLog entry = parseLogLine(line);
        if (!entry.ip.empty())
            logs.push_back(entry);
    }

    file.close();

    analyzeLogs(logs, argv[2]);
    cout << "Analysis complete. Report generated. \n";
    system("python visualize.py");    

    return 0;
}
