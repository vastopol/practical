class Solution
{
    public:
        bool judgeCircle(string moves)
        {
            int x = 0;
            int y = 0;
            bool b = false;
            for(char c : moves)
            {
                if(c == 'U')
                    y++;
                if(c == 'D')
                    y--;
                if(c == 'R')
                    x++;
                if(c == 'L')
                    x--;
            }
            if(x == 0 && y == 0)
                b = true;
            return b;
        }
};