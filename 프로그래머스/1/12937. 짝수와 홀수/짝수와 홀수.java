import java.io.*;
import java.util.*;
class Solution {
    public String solution(int num) throws IOException{
        String answer = "";
        if (num % 2 == 0){
            answer = "Even";
        }
        else{
            answer = "Odd";
        }
        return answer;
    }
}