import java.util.Scanner;
import static java.lang.Math.max;

public class Main {
    int filas;
    int columnas;

    public Main(){
        Scanner s = new Scanner(System.in);
        do{
            filas = s.nextInt();
            columnas = s.nextInt();

            if (filas == 0 && columnas == 0){
                break;
            }

            int vSol[] = new int[filas+2];
            int mat[][] = new int [filas][columnas+2];
            for(int i=0; i<filas; i++){
                for(int j=1; j<(columnas+1); j++){
                    mat[i][j] = s.nextInt();
                }
            }

            for(int i=0; i<filas; i++){
                for(int j=1; j<(columnas+1); j++){
                    mat[i][j+1] = max(mat[i][j],mat[i][j-1]+mat[i][j+1]);
                }
            }

            for (int i = 1; i < filas+1; i++) {
                vSol[i] = mat[i-1][columnas+1];
            }

            for (int i = 1; i < filas+1; i++) {
                vSol[i+1] = max(vSol[i],vSol[i-1]+vSol[i+1]);
            };
            System.out.println(vSol[filas+1]);
        }while(filas!=0 && columnas!=0);
    }

    public static void main(String[] args) {
        Main d = new Main();
    }

}
