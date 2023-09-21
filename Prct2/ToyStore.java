package Prct2;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;  
import java.util.List; 

public class ToyStore {
    private List<Toy> toys;  
  
    public ToyStore() {  
        this.toys = new ArrayList<>();  
    }  
  
    public void addToy(Toy toy) {  
        toys.add(toy);  
    }  
  
    public void updateToyWeight(int toyId, int weight) {  
        Toy toy = getToyById(toyId);  
        if (toy != null) {  
            toy.setWeight(weight);  
        }  
    }  
  
    public Toy choosePrizeToy() {  
        int totalWeight = calculateTotalWeight();  
        int randomWeight = (int) (Math.random() * totalWeight) + 1;  
        for (Toy toy : toys) {  
            randomWeight -= toy.getWeight();  
            if (randomWeight <= 0) { 
                toy.decreaseQuantity();
                if (toy.getQuantity() <= 0){
                    toys.remove(toy); 
                }  
                writeToFile(toy);  
                return toy;  
            }  
        }  
        return null;  
    }  
  
    private int calculateTotalWeight() {  
        int totalWeight = 0;  
        for (Toy toy : toys) {  
            totalWeight += toy.getWeight();  
        }  
        return totalWeight;  
    }
    public String getToyList() {  
        StringBuilder sb = new StringBuilder();  
        if (toys.size() > 0){
            for (Toy toy : toys) {  
                sb.append("ID: ").append(toy.getId())  
                .append(", Название: ").append(toy.getName())  
                .append(", Количество: ").append(toy.getQuantity())  
                .append(", Частота выпадения игрушки: ").append(toy.getWeight()).append("%\n");  
                }  
            return sb.toString();
        }else{
            return "Список пуст!";
        }
          
    }  
  
    private Toy getToyById(int toyId) {  
        for (Toy toy : toys) {  
            if (toy.getId() == toyId) {  
                return toy;  
            }  
        }  
        return null;  
    }  
  
    private void writeToFile(Toy toy) {  
    try (FileOutputStream fileOutputStream = new FileOutputStream("prize_toys.txt", true);  
         OutputStreamWriter writer = new OutputStreamWriter(fileOutputStream, StandardCharsets.UTF_8)) {  
        writer.write(toy.getName() + "\n");  
    } catch (IOException e) {  
        e.printStackTrace();  
    }  

    
} 
}
