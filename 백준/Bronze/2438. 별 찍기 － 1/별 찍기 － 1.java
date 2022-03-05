import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int i = sc.nextInt();
        for(int k=0 ; k<i ; k++){
        	for(int a=0 ; a<k ; a++) {
        		System.out.print("*");
        	}
            System.out.println("*");
        }
    }
}