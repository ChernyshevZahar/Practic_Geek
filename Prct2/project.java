package Prct2;

import java.util.Scanner;


public class project {

    public static void main(String[] args) {
        ToyStore toyStore = new ToyStore();   
        boolean exit = false;
        Scanner scanner = new Scanner(System.in,"Cp866");
  
        while (!exit) {  
            System.out.println("\nМеню:"); 

            System.out.println("1. Добавить игрушку");  
            System.out.println("2. Вывести список игрушек");  
            System.out.println("3. Изменить вес игрушки");  
            System.out.println("4. Розыгрыш игрушки");  
            System.out.println("5. Выйти из программы");
            // System.out.println("6. Добавить примеры игрушек для теста"); // для удобства чтоб не заполнять игрушки 
            System.out.print("Введите номер пункта меню: ");
            
            
            int choice = scanner.nextInt();
            
 
            switch (choice) {  
                case 1:
        
                    System.out.print("Введите id игрушки: ");  
                    int id = scanner.nextInt();  
                
                    scanner.nextLine();  
                    System.out.print("Введите название игрушки: ");  
                    String name = scanner.nextLine();  
                    System.out.print("Введите количество игрушек: ");  
                    int quantity = scanner.nextInt();  
                    System.out.print("Введите вес игрушки: ");  
                    int weight = scanner.nextInt();  
                    
                    Toy toy = new Toy(id, name, quantity, weight);  
                    toyStore.addToy(toy);  
                    System.out.println("\n Игрушка успешно добавлена.");
                    break; 
                      
                             
                case 2:  
                    System.out.println("Список игрушек:\n" + toyStore.getToyList());  
                    break;  
                      
                case 3:  
                    System.out.print("Введите id игрушки: ");  
                    int toyId = scanner.nextInt();  
                    System.out.print("Введите новый вес игрушки: ");  
                    int newWeight = scanner.nextInt();  
                    toyStore.updateToyWeight(toyId, newWeight);  
                    System.out.println("\nВес игрушки успешно изменен."); 
                    break;  
                      
                case 4:  
                    Toy prizeToy = toyStore.choosePrizeToy();  
                    if (prizeToy != null) {  
                        System.out.println("Выиграли игрушку: " + prizeToy.getName());  
                    } else {  
                        System.out.println("Игрушки закончились");  
                    }  
                    break;  
                      
                case 5:  
                    exit = true;  
                    System.out.println("\nПрограмма завершена.");  
                    break;  
                case 6:
                    Toy toy1 = new Toy(1, "Кукла", 5, 30);  
                    Toy toy2 = new Toy(2, "Мяч", 10, 20);  
                    Toy toy3 = new Toy(3, "Машинка", 8, 10);
                    toyStore.addToy(toy1);  
                    toyStore.addToy(toy2);  
                    toyStore.addToy(toy3);
                    break; 
                    
                default:
                    System.out.println("Нет такого выбора");
                  
            } 

        }
        scanner.close();
    }
}


