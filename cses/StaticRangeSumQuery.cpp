#include <bits/stdc++.h>

#define Log(x) for(auto e : x){ std::cout << e << " ";} std::cout << "\n";

int main(){
    long n, q;
    std::cin >> n;
    std::cin >> q;
    std::vector<long> v;
    std::vector<std::pair<long, long>> pairs;
    std::vector<long> prefix(n + 1);
    for(long i = 0; i < n; i++ ){
        long val;
        std::cin >> val;
        v.push_back(val);
    }

    for(long i = 0; i < q; i++){
        long first, second;
        std::cin >> first;
        std::cin >> second;
        pairs.push_back(std::pair<int,int>(first, second));
    }

    for(int i = 0; i < n; i++){
        prefix[i + 1] += v[i] + prefix[i];
    }

    for(auto p : pairs){
        std::cout << (prefix[p.second]  - prefix[p.first - 1]) << "\n";
    }
}
