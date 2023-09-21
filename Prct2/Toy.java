package Prct2;

/**
 * 
 * Класс создания игрушек
 * 
 * id- id в системе,
 * name - название игрушки,
 * quantity - количество игрешек,
 * weight - частота выпадения игрушки,
 * 
 */



public class Toy {
    private int id;  
    private String name;  
    private int quantity;  
    private int weight;  
  
    public Toy(int id, String name, int quantity, int weight) { 
         
        this.id = id;  
        this.name = name;  
        this.quantity = quantity;  
        this.weight = weight;  
    }  
  
    public int getId() {  
        return id;  
    }  
  
    public String getName() {  
        return name;  
    }  
  
    public int getQuantity() {  
        return quantity;  
    }  
  
    public int getWeight() {  
        return weight;  
    }  
  
    public void setWeight(int weight) {  
        this.weight = weight;  
    }  
  
    public void decreaseQuantity() {  
        this.quantity = this.quantity - 1;  
    }  
}
