class Solution {
public:
    int longestMountain(vector<int>& arr) {
        int n = arr.size();
        int i=1;
        int upper,lower;
        int ans = 0;
        
        while(i<n)
        {
            upper = 0;lower = 0; 
            while(i<n && arr[i-1] == arr[i])
                i++;
            while(i<n && arr[i-1] < arr[i])
            {
                upper++;
                i++;
            }
            while(i<n && arr[i-1] > arr[i])
            {
                lower++;
                i++;
            }
            if(upper && lower)
                ans = max(ans, upper+lower+1);
        }
        return ans;
        
    }
};
