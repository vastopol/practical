#include <map>
class Solution
{
    public:

        int numJewelsInStones(string J, string S)
        {
            map<char,int> counter;
            int total = 0;

            for(char c : S)
            {
                counter[c] += 1;
            }

            for(char c : J)
            {
                total += counter[c];
            }

            return total;
        }
};