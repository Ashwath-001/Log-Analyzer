#include <unordered_map>
#include <vector>
#include <fstream>
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

void analyzeLogs(const vector<AccessLog>& logs, const string& reportPath) {

    unordered_map<string, int> ipHits;
    unordered_map<string, int> urlHits;
    unordered_map<int, int> statusCount;

    for (const auto& log : logs) {
        ipHits[log.ip]++;
        urlHits[log.url]++;
        statusCount[log.status]++;
    }

    ofstream report(reportPath);

    report << "===== WEB ACCESS LOG REPORT =====\n\n";
    report << "Total Requests: " << logs.size() << "\n\n";

    report << "Top IP Addresses:\n";
    for (auto& ip : ipHits) {
        if (ip.second >= 5)
            report << "- " << ip.first << " : " << ip.second << " requests\n";
    }

    report << "\nMost Accessed URLs:\n";
    for (auto& url : urlHits) {
        if (url.second >= 3)
            report << "- " << url.first << " : " << url.second << " hits\n";
    }

    report << "\nHTTP Status Codes:\n";
    for (auto& s : statusCount) {
        report << "- " << s.first << " : " << s.second << "\n";
    }

    report << "\nSuspicious Activity:\n";
    for (auto& ip : ipHits) {
        if (ip.second > 20) {
            report << "- Possible abuse from IP: " << ip.first << "\n";
        }
    }

    report << "\n===== END OF REPORT =====\n";

    ofstream csv("report.csv");
    csv << "type,key,value\n";

    for (auto& ip : ipHits)
        csv << "IP," << ip.first << "," << ip.second << "\n";

    for (auto& url : urlHits)
        csv << "URL," << url.first << "," << url.second << "\n";

    for (auto& s : statusCount)
        csv << "STATUS," << s.first << "," << s.second << "\n";

    csv.close();
}
