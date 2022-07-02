import java.util.*;

class Main {
    public static void main(String[] args) {
        Database database_clothes = new Database();
        List<List<String>> list_2D;
        list_2D = database_clothes.Get("select * from clothes");
        System.out.println(list_2D);
        database_clothes.Close();
    }
}