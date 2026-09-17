package br.com.grancursosonline.faculdade;

import java.util.Scanner;

public class Principal {
    public static void main(String[] args) {
        Integer a, b, resposta; 

        String nome = "";

        Double percentual;

        Scanner in = new Scanner (System.in);
        // "in" é o nome dado à variável Scanner, usado aqui como abreviação de input (entrada);
        // System.in é a entrada padrão do Java, normalmente o teclado.

        System.out.print("Digite o primeiro número: ");
        // print() imprime e permanece na mesma linha; println() imprime e pula para a próxima linha.
        a = in.nextInt();
        // nextInt() lê o próximo número inteiro digitado pelo usuário.

        System.out.print("Digite o segundo número: ");
        b = in.nextInt();

        System.out.print("Digite o seu nome: ");
        nome = in.next();
        // next() lê o próximo texto digitado pelo usuário. Lê até encontrar um espaço.
        // nextLine() lê uma linha inteira de texto, incluindo os espaços.

        System.out.print("Digite um número percentual: ");
        percentual = in.nextDouble();
        // nextDouble() lê o próximo número decimal digitado pelo usuário.
        // Neste ambiente, o separador decimal é ponto (ex.: 5.8).

        in.close();
        // Fecha o Scanner após o término das leituras.

        resposta = a + b;

        System.out.println("A soma dos números é: " + resposta);
        // O operador + concatena (junta) o texto com o valor da variável resposta.

        System.out.println("Quem escreveu foi: " + nome);

        System.out.println(percentual);
    }
}