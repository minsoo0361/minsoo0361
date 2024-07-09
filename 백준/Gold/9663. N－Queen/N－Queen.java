import org.w3c.dom.Node;

import java.io.*;
import java.util.*;

import static java.util.Arrays.sort;

public class Main {

    static Boolean[] c = new Boolean[31], c1 = new Boolean[31], c2 = new Boolean[31];
    static int ans = 0, n;

    static void go(int idx) {
        if(idx >= n){
            ans++;
            return;
        }
        for(int i=0;i<n;i++){
            if(c[i])continue;
            if(c1[idx+i])continue;
            if(c2[i-idx+n])continue;
            c[i]=c1[idx+i]=c2[i-idx+n]=true;
            go(idx+1);
            c[i]=c1[idx+i]=c2[i-idx+n]=false;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        n = Integer.parseInt(br.readLine());
        for(int i=0;i<31;i++)c[i]=c1[i]=c2[i]=false;
        go(0);
        bw.write(ans+"");
        br.close();
        bw.flush();
        bw.close();

    }


}
