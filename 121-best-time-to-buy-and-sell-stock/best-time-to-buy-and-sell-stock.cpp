class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buytime = prices[0];
        int selltime = 0;
        for(int i=0;i<prices.size();i++){
            buytime = min(buytime, prices[i]);
            selltime = max(selltime, prices[i]-buytime);
        }
        return selltime;
    }
};