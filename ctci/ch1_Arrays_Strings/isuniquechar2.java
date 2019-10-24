/*

assumes lowercase
reduce the space usage by factor of 8 -> bit vector
this uses an int as the bit vector
checks the char - 'a' anded with the int to look at position
if not in vector then or the bit into the vector

*/

boolean isUniqueChars(String str)
{
    int checker = 0;
    
    for(int i = 0; i < str.length(); i++)
    {
        int val  = str.charAt(i) - 'a';
        if((checker & (1 << val)) > 0)
        {
            return false;
        }
        checker |= (1 << val);
    }
    return true;
}
