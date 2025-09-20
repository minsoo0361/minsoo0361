import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String st = br.readLine();
        int [] word = new int [26];
        for (int i = 0; i < st.length(); i++){
            if (65 <= st.charAt(i) && st.charAt(i) <= 90){
                word[st.charAt(i) - 65] ++;
            }
            else{
                word[st.charAt(i) - 97] ++;
            }
        }

        int num = -1;
        char ch = '?';

        for (int i = 0; i < 26; i++){
            if (word[i] > num){
                num = word[i];
                ch = (char) (i + 65);
            }
            else if(word[i] == num){
                ch = '?';
            }
        }
        System.out.print(ch);
    }
}
