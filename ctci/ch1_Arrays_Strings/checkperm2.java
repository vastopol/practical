/*

assume ascii
array that maps the chars to their frequency
increment through the forst string
decrement throught the second string
at the end they should be all zeros

*/

boolean permutation(String s, String t)
{
    if(s.length() != t.length())
    {
        return false;
    }

    int[] letters = new int[128];

    for(int i = 0; i < s.length(); i++)
    {
        letters[s.charAt(i)]++;
    }

    for(int i = 0; i < t.length(); i++)
    {
        letters[t.charAt(i)]--;
        if(letters[t.charAt(i)] < 0)
        {
            return false;
        }
    }

    return true;
}
