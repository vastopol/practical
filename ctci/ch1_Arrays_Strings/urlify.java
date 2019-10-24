/*

replace ' ' with "%20"
string has extra spacess at the end as a temp buffer
modify in place working backwards

use the char array in java

uses a 2 scan approach to replacing
first scan count the number of spaces
next triple this number to get number of extra characters
second scan in reverse edit the string
if see space replace with %20
else copy the original char

*/

void replaceSpaces(char[] str, int trueLength)
{
    int spaceCount = 0;
    int index = 0;
    int i = 0;

    for(i = 0; i < trueLength; i++)
    {
        if(str[i] == ' ')
        {
            spaceCount++;
        }
    }

    index = trueLength + spaceCount * 2;

    if(trueLength < str.length()) // end array
    {
        str[trueLength] = '\0';
    }
    for(i = trueLength - 1; i >= 0; i--)
    {
        if(str[i] = ' ')
        {
            str[index - 1] = '0';
            str[index - 2] = '2';
            str[index - 3] = '%';
            index -= 3;
        }
        else
        {
            str[index-1] = str[i];
            index--;
        }
    }
}