# Brackets.py


&nbsp; A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

   &nbsp; <br />      S is empty;
  &nbsp;  <br />      S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
  &nbsp;   <br />    S has the form "VW" where V and W are properly nested strings.

&nbsp;For example, the string "{[()()]}" is properly nested but "([)()]" is not.

&nbsp; Write a function:

  &nbsp; <br />   class Solution { public int solution(String S); }

&nbsp; that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

&nbsp; For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

&nbsp; Write an efficient algorithm for the following assumptions:

  &nbsp; <br />      N is an integer within the range [0..200,000];
    &nbsp; <br />    string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".

