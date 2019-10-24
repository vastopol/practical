/*

assume ascii 128 chars 2^7
time complexity is O(n), n is length of String
space complexity is O(1)

*/

boolean isUniqueChars(String str)
{
    if(str.length() > 128)
    {
        return false;
    }

    boolean[] char_set = new boolean[128];
    
    for(int i = 0; i < str.length(); i++)
    {
        int val = str.charAt(i);
        if(char_set[val])  // already found char in string
        {
            return false;
        }
        char_set[val] = true;
    }
    return true;
}
