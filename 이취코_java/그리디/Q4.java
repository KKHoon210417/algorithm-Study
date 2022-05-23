import java.util.*;

public class Q4{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // n, k을 공백 기준으로 구분하여 받기
        int n = sc.nextInt();
        int k = sc.nextInt();
        int result = 0;

        while(n > 1) {
            if (n%k == 0) {
                n = n / k;
            } else {
                n = n - 1;
            }
            result += 1;
        }
        System.out.println(result);
    }
}