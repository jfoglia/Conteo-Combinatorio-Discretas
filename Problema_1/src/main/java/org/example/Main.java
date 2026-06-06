package org.example;

import java.math.BigInteger;
import java.util.Scanner;
import com.google.common.math.BigIntegerMath;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("\t\t\tBienvenido a la mejor Calculadora de permutaciones y k-permutaciones!!");

        int[] valores = pedirValores(sc);

        while (!validar(valores[0], valores[1])) {

            System.out.println("\nValores inválidos. Intenta nuevamente.\n");

            valores = pedirValores(sc);
        }

        // Metodo 1: factorial iterativo propio
        BigInteger resultadoIterativo = permutacionIterativa(valores[0], valores[1]);

        // Metodo 2: usando BigIntegerMath
        BigInteger resultadoLibreria = permutacionLibreria(valores[0], valores[1]);

        mostrarResultado(
                valores[0],
                valores[1],
                resultadoIterativo,
                resultadoLibreria
        );

        sc.close();
    }

    private static int[] pedirValores(Scanner sc) {

        System.out.println("Por favor ingresa los valores de n y de r:");

        System.out.print("n: ");
        int n = sc.nextInt();

        System.out.print("r: ");
        int r = sc.nextInt();

        return new int[]{n, r};
    }

    private static boolean validar(int n, int r) {

        if (n < 0) {

            System.out.println("n no puede ser negativo.");
            return false;
        }

        if (r < 0) {

            System.out.println("r no puede ser negativo.");
            return false;
        }

        if (r > n) {

            System.out.println("r no puede ser mayor que n.");
            return false;
        }

        return true;
    }

    // =========================
    // PERMUTACIÓN - MÉTODO 1
    // =========================

    private static BigInteger permutacionIterativa(int n, int r) {

        BigInteger factorialN = factorialIterativo(n);

        BigInteger factorialNR = factorialIterativo(n - r);

        return factorialN.divide(factorialNR);
    }

    // =========================
    // PERMUTACIÓN - MÉTODO 2
    // =========================

    private static BigInteger permutacionLibreria(int n, int r) {

        BigInteger factorialN = BigIntegerMath.factorial(n);

        BigInteger factorialNR = BigIntegerMath.factorial(n - r);

        return factorialN.divide(factorialNR);
    }

    // =========================
    // FACTORIAL ITERATIVO
    // =========================

    private static BigInteger factorialIterativo(int numero) {

        BigInteger resultado = BigInteger.ONE;

        for (int i = 1; i <= numero; i++) {

            resultado = resultado.multiply(BigInteger.valueOf(i));
        }

        return resultado;
    }

    private static void mostrarResultado(
            int n,
            int r,
            BigInteger resultadoIterativo,
            BigInteger resultadoLibreria
    ) {

        System.out.println("\n====================================");
        System.out.println("Procedimiento");
        System.out.println("====================================");

        System.out.println("P(" + n + ", " + r + ") = " + n + "! / (" + n + " - " + r + ")!");

        System.out.println("P(" + n + ", " + r + ") = " + n + "! / " + (n - r) + "!");

        System.out.println("\n====================================");
        System.out.println("Resultados");
        System.out.println("====================================");

        System.out.println("Método iterativo: " + resultadoIterativo);

        System.out.println("Método usando librería: " + resultadoLibreria);
    }
}