class Solution
{
    public:
    void reverseString(vector<char>& s)
    {
        int half = s.size()/2;
        for(int i = 0; i < half; i++)
        {
            char a = s[i];
            char b = s[s.size()-1-i];
            s[i] = b;
            s[s.size()-1-i] = a;
        }
    }
};