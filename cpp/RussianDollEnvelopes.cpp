#include <bits/stdc++.h>


using namespace std;


int dp(int pos, int last_used, vector<vector<int>>& e, vector<vector<int>>& memo){

    if(pos == e.size()){
        return 0;
    }

    if(memo[pos][last_used + 1] != -1){
        return memo[pos][last_used + 1];
    }

    // skip
    int skip = dp(pos + 1,last_used,e,memo);


    // take
    int take = 0;
    int current_width = e[pos][0];
    int current_height = e[pos][1];


    if (last_used == -1){
        take = 1 + dp(pos+1,pos,e,memo);
    }else if(last_used != -1){
        int prev_width = e[last_used][0];
        int prev_height = e[last_used][1];
        if(prev_width < current_width && prev_height < current_height){
            take = 1 + dp(pos+1,pos,e, memo);
        }
    }

    int res = max(take,skip);
    memo[pos][last_used + 1] = res;
    return res;
}

int maxEnvelopes(vector<vector<int>>& envs) {

        // [[5,4],[6,4],[6,7],[2,3]]
        // [[2,3],[5,4],[6,4],[6,7]]
        // [[1,1],[1,1], [1,1]]
        // [[1,1]] -> 1
        // [[1,1],[2,2]]
        // Greedy does not work
        // Try take it or leave it DP will work here
        // Greedy instinct will be to sort the array and then try and fit
        // the smallerone with neighbor assuming it will fit
        // The i + 1 envelope might not work so we skip it and next
        // starting from the smallest we
        // [1,1]
        // [3,3],[5,4],[6,4],[6,7]
        std::sort(envs.begin(), envs.end());
        int n = envs.size();
        vector<vector<int>> memo(n + 1, vector<int>(n + 1,-1));
        return dp(0,-1,envs,memo);
}

int main(){
    vector<vector<int>> envs1 = {{5,4}, {6,4}, {6,7}, {2,3}};
    // vector<vector<int>> envs2 = {{1,1}, {1,1}, {1,1}};
    vector<vector<int>> envs3 = {{1,4}, {2,3}, {4,5}, {5,6}, {2,7}};
    cout << "Result is " << maxEnvelopes(envs3) << endl;
}
